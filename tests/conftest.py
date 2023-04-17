import pytest
from transformers import AutoModel


@pytest.fixture
def model():
    # TODO: load model from checkpoint
    return AutoModel.from_pretrained("gpt2")
