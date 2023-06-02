import pytest
from transformers import AutoModel
from xprodgpt.tokenizer import create_tokenizer
from xprodgpt.utils import load_yaml


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
