from prodgpt.data.data_warehouse import DataWarehouse, TrainingText

EXAMPLE_TEXTS = [
    "Persistence is all you need",
    "The best way to predict the future is to invent it",
    "The best way to predict the future is to invent it",
]


def test_data_model():
    UUID_LENGTH = 36
    data = TrainingText(text="Persistence is all you need")

    assert isinstance(data.uuid, str)
    assert len(data.uuid) == UUID_LENGTH
    assert isinstance(data.text, str)
    assert data.text == "Persistence is all you need"
    assert isinstance(data.created_at, str)
    assert data.updated_at is None
    assert data.deleted_at is None
    assert data.is_deleted is False


def test_add_extract_delete_data_to_data_warehouse(config):
    data = [TrainingText(text=x) for x in EXAMPLE_TEXTS]
    # data_uuids = [x.uuid for x in data]

    data_warehouse = DataWarehouse(config)

    output = data_warehouse.insert(data)

    assert output is True

    # extracted_data = data_warehouse.extract_from_uuid(data_uuids)

    pass
    # assert len(extracted_data) == len(data_uuids)

    # output = data_warehouse.delete(data_uuids)
