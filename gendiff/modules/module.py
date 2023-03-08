UNCHANGED = "  "
NEW = "+ "
OLD = "- "


def compare(dict1: dict, dict2: dict):
    result = {}
    union_keys = dict1.keys() & dict2.keys()
    only_first = dict1.keys() - dict2.keys()
    only_second = dict2.keys() - dict1.keys()

    for key in sorted(union_keys):
        if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result[key] = {
                "key": key,
                "status": "nested",
                "value": compare(dict1[key], dict2[key])}
        elif dict1[key] == dict2[key]:
            result[key] = {
                "key": key,
                "value": dict1[key],
                "status": UNCHANGED}
        else:
            result[key] = {"key": key, "status": "difference",
                           "old_value": dict1[key],
                           "new_value": dict2[key]}

    for key in sorted(only_first):
        result[key] = {"key": key,
                       "value": dict1[key],
                       "status": OLD}
    for key in sorted(only_second):
        result[key] = {"key": key,
                       "value": dict2[key],
                       "status": NEW}
    return dict(sorted(result.items()))
