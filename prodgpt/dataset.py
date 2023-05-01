from datasets import load_dataset
from torch.utils.data import Dataset


def create_dataset(config, tokenizer) -> Dataset:
    DATASET_PATH = config["dataset"]["path"]
    COL_NAMES_REMOVE = ["text", "label"]

    dataset = load_dataset(DATASET_PATH)

    def tokenize_text(x):
        return tokenizer(x["text"], padding="max_length", truncation=True)

    tokenized_dataset = dataset.map(tokenize_text, batched=True)
    tokenized_dataset = tokenized_dataset.remove_columns(COL_NAMES_REMOVE)
    return tokenized_dataset
