from xprodgpt.dataset import create_dataset


def test_create_dataset(config, tokenizer):
    EXPECTED_COLS = ["attention_mask", "input_ids"]

    dataset = create_dataset(config, tokenizer)

    assert "train" in dataset.keys()
    assert len(dataset["train"]) > 0
    assert len(dataset["train"].features.keys()) == len(EXPECTED_COLS)
    assert all([x in dataset["train"].features.keys() for x in EXPECTED_COLS])
