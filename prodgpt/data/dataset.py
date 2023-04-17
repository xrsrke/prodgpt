from typing import Iterable, List

import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer


class TextDataset(Dataset):
    def __init__(
        self,
        data: Iterable,  # local path to the dataset
        tokenizer: AutoTokenizer
    ) -> None:
        super().__init__()

        tokenized_data = tokenizer(
            data,
            return_tensors="pt",
            padding="max_length",
            truncation=True
        )

        data = []
        for input_ids in tokenized_data:
            x = input_ids[:, :-1]
            y = input_ids[:, 1:].clone()
            data.append(x, y)
        self.data = data

    def __getitem__(self, index) -> List[torch.Tensor, torch.Tensor]:
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)
