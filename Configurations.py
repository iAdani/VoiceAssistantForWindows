import yaml
import os
from shutil import copyfile


# Check if configurations file already exists, if not - load the defaults
if not os.path.exists("config.yaml"):
    copyfile("defaultConfig.yaml", "config.yaml")


# Load configurations
def load_config():
    with open("config.yaml") as c:
        global config
        config = yaml.safe_load(c)


config = {}
load_config()


# Change preferred voice
def change_voice(i):
    old = config["voice"]
    with open("config.yaml", "w") as conf:
        config["voice"] = i
        try:
            yaml.safe_dump(config, conf, default_flow_style=False)
        except:
            config["voice"] = old


def get_voice():
    return config["voice"]