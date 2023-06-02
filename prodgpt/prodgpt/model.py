from transformers import AutoConfig, AutoModelForPreTraining, AutoTokenizer


def get_model(config, tokenizer: AutoTokenizer):
    model_path = config["model"]["path"]
    model_config = AutoConfig.from_pretrained(
        model_path,
        pad_token_id=tokenizer,
        output_hidden_states=True
    )

    model = AutoModelForPreTraining.from_pretrained(
        model_path,
        config=model_config
    )
    return model
