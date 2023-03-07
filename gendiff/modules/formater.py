import json


def format_flat_json(data: dict) -> dict:
    result = {}
    for k, v in sorted(data.items()):

        if v['status'] == 'nested':
            result[k] = format_flat_json(v['value'])

        elif v['status'] == 'difference':
            result['- ' + v['key']] = v['old_value']
            result['+ ' + v['key']] = v['new_value']
        else:
            result[v['status'] + k] = v['value']
    return result


def show_result(data: dict) -> str:
    diff = format_flat_json(data)
    diff_json = json.dumps(diff, indent=2)
    return diff_json.replace('"', '')
