import yaml


def get_data():
    f = open("../config/data.yaml", encoding="utf8")
    data = yaml.safe_load(f)
    return data
