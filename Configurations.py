import yaml
import os
from shutil import copyfile


# Check if configurations file already exists, if not - load the defaults
if not os.path.exists("config.yaml"):
    copyfile("defaultConfig.yaml", "config.yaml")


# Restore the default configurations
def restore_default_config():
    copyfile("defaultConfig.yaml", "config.yaml")


# Load configurations
def load_config():
    with open("config.yaml") as c:
        global config
        config = yaml.safe_load(c)


config = {}
load_config()


# Change preferred voice
def change_voice():
    old = config["voice"]
    with open("config.yaml", "w") as conf:
        config["voice"] = 1 - config["voice"]
        try:
            yaml.safe_dump(config, conf, default_flow_style=False)
        except:
            config["voice"] = old


# Returns the type of the current theme
def get_theme_type():
    return config["theme"]


# Set a new theme type
def set_theme_type(theme_type):
    old = config["theme"]
    with open("config.yaml", "w") as conf:
        config["theme"] = theme_type
        try:
            yaml.safe_dump(config, conf, default_flow_style=False)
        except:
            config["theme"] = old


# Returns the configurations of a theme
def get_theme_config(theme_type):
    with open("themes.yaml", "r") as themes:
        theme = yaml.safe_load(themes)
        return theme[theme_type]


# Returns the current voice configuration
def get_voice():
    return config["voice"]