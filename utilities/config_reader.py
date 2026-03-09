import yaml
import os

def get_config():
    # Correct path to config/config.yaml
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config["environments"]["qa"]

