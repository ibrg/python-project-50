from gendiff.modules.parse import read_file

UNCHANGED = ' '
NEW = '+'
OLD = '-'


def compare(first_file: str, second_file: str):
    first = read_file(first_file)
    second = read_file(second_file)
    result = {}
    # find keys that have in both files
    # find keys that have in first but hasn't a second file
    # find keys that have only second file
    # check values for all keys in sets

    union_keys = first.keys() & second.keys()
    only_first = first.keys() - second.keys()
    only_second = second.keys() - first.keys()

    for key in sorted(union_keys):
        if first[key] == second[key]:
            result[key] = {'value': first[key], 'status': UNCHANGED}
        else:
            result[key] = {'value': first[key], 'status': OLD}
            result[key + ' '] = {'value': second[key], 'status': NEW}
    for key in sorted(only_first):
        result[key] = {'value': first[key], 'status': OLD}
    for key in sorted(only_second):
        result[key] = {'value': second[key], 'status': NEW}
    return dict(sorted(result.items()))
