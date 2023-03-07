import json


def format(data: dict) -> dict:
    result = {}
    for k, v in sorted(data.items()):
        if v['status'] == 'nested':
            result[k] = format(v['value'])

        if v['status'] == 'difference':
            result['- ' + v['key']] = v['old_value']
            result['+ ' + v['key']] = v['new_value']
        else:
            result[v['status'] + k] = v['value']
    return result


def stylish_format(data: dict) -> str:
    diff = json.dumps(format(data), indent=4)
    return diff.replace('"', '')


def json_format(data: dict):
    return json.dumps(data, indent=4)
