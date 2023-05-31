import pytest

from prodgpt.data.extractor import RandomExtractor


@pytest.mark.skip(reason="Not implemented")
def test_random_extract_from_n_tokens():
    N_TOKENS = 300_000_000

    extractor = RandomExtractor(n_tokens=N_TOKENS)

    assert len(extractor) == N_TOKENS


def test_to_training_data():
    N_TOKENS = 1000
    extractor = RandomExtractor(n_tokens=N_TOKENS)
    training_data, validation_data = extractor.to_training_data()

    assert len(training_data) + len(validation_data) == N_TOKENS
