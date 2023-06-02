from transformers import AutoTokenizer


def create_tokenizer(config) -> AutoTokenizer:
    TOKENIZER_PATH = config["tokenizer"]["path"]

    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    tokenizer.pad_token = tokenizer.eos_token

    return tokenizer
