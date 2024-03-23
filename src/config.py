# import os module & the OpenAI Python library for calling the OpenAI AP
import yaml


def read_conf():
    with open('conf/config.yaml') as f:
        conf = yaml.safe_load(f)
    return conf
