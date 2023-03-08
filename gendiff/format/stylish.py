def check(value):
    # Func to check dict value
    res = ''
    if isinstance(value, bool):
        res = str(value).lower()
    elif value is None:
        res = 'null'
    else:
        res = value
    return res


def tree(element, depth=1):
    if isinstance(element, dict):
        string = ['{']
        for key, value in element.items():
            string.append(
                '\n' + '  ' * depth + '  ' + str(key) + ': ' + str(
                    tree(value, depth + 2)))
        string.append('\n' + '  ' * (depth - 1) + '}')
        result = ''.join(string)
        return result
    else:
        return check(element)


def stylish(diff, depth=1):
    line = []
    for k, v in diff.items():
        if v['status'] == 'nested':
            line.append('  ' * depth + '  ' + k + ': {' '\n')
            line.append(stylish(v['value'], depth + 2))
            line.append('  ' * (depth + 1) + '}' + '\n')
        elif v['status'] == 'difference':
            old = str(tree(v['old_value'], depth + 2))
            new = str(tree(v['new_value'], depth + 2))
            line.append('  ' * depth + '- ' + k + ': ' + old + '\n')
            line.append('  ' * depth + '+ ' + k + ': ' + new + '\n')
        else:
            val = str(tree(check(v['value']), depth + 2))
            line.append('  ' * depth + v['status'] + k + ': ' + val + '\n')
    result = ''.join(line)
    return result


def stylish_format(diff):
    diff = stylish(diff)
    result = '{' + '\n' + diff + '}'
    return result
