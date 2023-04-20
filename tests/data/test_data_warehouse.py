import uuid

from prodgpt.data.data_warehouse import DataBatch, DataWarehouse, TrainingText

EXAMPLES = [
    "Persistence is all you need",
    "The best way to predict the future is to invent it",
    "The best way to predict the future is to invent it",
]


def test_data_batch_model():
    UUID = str(uuid.uuid4())
    NAME = "test"

    batch = DataBatch(uuid=UUID, name=NAME)

    assert batch.uuid == UUID
    assert batch.name == NAME


def test_data_training_text_model():
    texts = [TrainingText(text=x) for x in EXAMPLES]

    for x in texts:
        # assert isinstance(x.uuid, str)
        # assert len(x.uuid) == 36
        assert isinstance(x.text, str)
        assert x.text in EXAMPLES


def test_add_extract_delete_data_to_data_warehouse(config):
    data = [TrainingText(uuid=str(uuid.uuid4()), text=x) for x in EXAMPLES]
    uuids = [x.uuid for x in data]
    data_warehouse = DataWarehouse(config)

    output = data_warehouse.insert(data)
    assert output is True

    extracted_data = data_warehouse.extract_from_uuid(uuids)
    assert len(extracted_data) == len(uuids)
    assert all([x.uuid in uuids for x in extracted_data])

    output = data_warehouse.delete_from_uuid(uuids)
    assert output is True
