import yaml


def load_yaml(path):
    """Load a yaml file."""
    with open(path, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
