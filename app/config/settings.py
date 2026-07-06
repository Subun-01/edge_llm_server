from pathlib import Path
import yaml


# Project root/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_PATH = PROJECT_ROOT / "configs" / "app.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


settings = load_config()