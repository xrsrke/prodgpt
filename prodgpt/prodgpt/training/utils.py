from datasets import load_dataset
from torch.utils.data import Dataset
from transformers import AutoModel, AutoTokenizer


def load_model(model_path: str = "gpt2"):
    return AutoModel.from_pretrained(model_path)


def load_tokenizer(tokenizer_path: str = "gpt2"):
    return AutoTokenizer.from_pretrained(tokenizer_path)


def load_tokenized_dataset() -> Dataset:
    return load_dataset('my_dataset')
