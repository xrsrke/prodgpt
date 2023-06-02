from datasets import load_dataset
from torch.utils.data import Dataset
from transformers import PretrainedTokenizerBase


def create_dataset(
    data_path: str,
    tokenizer: PretrainedTokenizerBase
) -> Dataset:
    COL_NAMES_REMOVE = ["text", "label"]

    dataset = load_dataset(data_path)

    def tokenize_text(x):
        return tokenizer(
            x["text"],
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

    tokenized_dataset = dataset.map(
        tokenize_text,
        batched=True,
        remove_columns=COL_NAMES_REMOVE
    )
    # tokenized_dataset = tokenized_dataset.remove_columns(COL_NAMES_REMOVE)
    return tokenized_dataset
