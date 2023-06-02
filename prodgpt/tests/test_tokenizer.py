from xprodgpt.tokenizer import create_tokenizer


def test_create_tokenizer(config):
    tokenizer = create_tokenizer(config)

    assert tokenizer.pad_token == tokenizer.eos_token
