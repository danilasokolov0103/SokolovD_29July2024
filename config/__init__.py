import os

from envyaml import EnvYAML


def load_config():
    configs = EnvYAML(os.path.join(os.path.dirname(__file__), "config.yaml"), strict=False)
    if STAND_TYPE not in configs:
        raise EnvironmentError("ENV variable not found")

    return configs[STAND_TYPE]


STAND_TYPE = os.environ.get("STAND_TYPE", "BASE")


config = load_config()
