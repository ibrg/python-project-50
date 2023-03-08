import json


def json_format(data: dict):
    return json.dumps(data, indent=4)
