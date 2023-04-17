import pytest
from transformers import AutoModel

from prodgpt.utils import load_yaml


@pytest.fixture
def config():
    return load_yaml("./configs/config.yaml")


@pytest.fixture
def model():
    # TODO: load model from checkpoint
    return AutoModel.from_pretrained("gpt2")
