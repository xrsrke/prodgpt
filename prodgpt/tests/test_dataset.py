from prodgpt.dataset import create_dataset


def test_create_dataset(config, tokenizer):
    EXPECTED_COLS = ["attention_mask", "input_ids"]
    DATA_PATH = config["dataset"]["path"]

    dataset = create_dataset(
        data_path=DATA_PATH,
        tokenizer=tokenizer
    )

    assert "train" in dataset.keys()
    assert len(dataset["train"]) > 0
    assert len(dataset["train"].features.keys()) == len(EXPECTED_COLS)
    assert all([x in dataset["train"].features.keys() for x in EXPECTED_COLS])
