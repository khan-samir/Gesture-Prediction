import os
import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))
CONFIG_PATH = os.path.join(dir_path, 'config.yml')


def read_params(config_path=CONFIG_PATH):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


if __name__ == '__main__':
    read_params()
