import json


def format(data: dict) -> dict:
    result = {}
    for k, v in sorted(data.items()):
        if v['status'] == 'nested':
            result[k] = format(v['value'])

        elif v['status'] == 'difference':
            result['- ' + v['key']] = v['old_value']
            result['+ ' + v['key']] = v['new_value']
        else:
            result[v['status'] + k] = v['value']
    return result


def stylish_format(data: dict) -> str:
    diff = json.dumps(format(data), indent=2)
    return diff.replace('"', '')
