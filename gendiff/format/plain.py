
def check(value):
    # Func to check dict value
    res = ''
    if isinstance(value, dict):
        res = '[complex value]'
    elif isinstance(value, bool):
        res = str(value).lower()
    elif value is None:
        res = 'null'
    elif isinstance(value, int):
        res = value
    else:
        res = f"'{value}'"
    return res


def plain_format(data: dict):
    def walk(node, path):
        result = ''
        for k, v in node.items():
            curr_path = f"{path}{v['key']}"
            if v['status'] == 'difference':
                result += f"Property '{curr_path}' was updated."
                result += f" From {check(v['old_value'])} to"
                result += f" {check(v['new_value'])}\n"
            elif v['status'] == '- ':
                result += f"Property '{curr_path}' was removed\n"
            elif v['status'] == "+ ":
                result += f"Property '{curr_path}'"
                result += f" was added with value: {check(v['value'])}\n"
            elif v['status'] == 'nested':
                result += walk(v['value'], curr_path + '.') + '\n'
        return result[:-1]
    return walk(data, '')
