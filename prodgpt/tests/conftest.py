import pytest
from transformers import AutoModel

from prodgpt.tokenizer import create_tokenizer
from prodgpt.utils import load_yaml


@pytest.fixture
def config():
    return load_yaml("./configs/default.yaml")


@pytest.fixture
def model():
    # TODO: load model from checkpoint
    return AutoModel.from_pretrained("gpt2")


@pytest.fixture
def tokenizer(config):
    return create_tokenizer(config)
