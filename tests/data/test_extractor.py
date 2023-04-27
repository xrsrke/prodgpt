from prodgpt.data.extractor import RandomExtractor


def test_random_extractor():
    N_TOKENS = 300_000_000

    extractor = RandomExtractor(n_tokens=N_TOKENS)

    assert len(extractor) == N_TOKENS
