from datasets import load_dataset
from transformers import AutoTokenizer

from prodgpt.data.dataset import TextDataset


def test_text_dataset():
    data = load_dataset("cc_news", streaming=True, split="train")
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    dataset = TextDataset(data, tokenizer)

    assert len(dataset) == 1000
