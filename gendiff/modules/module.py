from .parse import read_file

UNCHANGE = ' '  # ключ есть в обоих файлах
REMOVE = '-'  # находится в первом файле
ADDED = '+'  # находится во втором файле


def check_key_in_dicts(dict1: dict, dict2: dict, keys: list) -> dict:
    result = {}
    for k in keys:
        if (k in dict1) and (k in dict2):
            if dict1[k] == dict2[k]:
                result[UNCHANGE + ' ' + k] = {"value": dict1[k]}
            elif dict1[k] != dict2[k]:
                result[REMOVE + ' ' + k] = {"value": dict1[k]}
                result[ADDED + ' ' + k] = {"value": dict2[k]}
        elif k in dict1 and k not in dict2:
            result[REMOVE + ' ' + k] = {"value": dict1[k]}
        elif k not in dict1 and k in dict2:
            result[ADDED + ' ' + k] = {"value": dict2[k]}
    return result


def compare(file1, file2):
    data_dict_a = read_file(file1)
    data_dict_b = read_file(file2)

    # Находим уникальные ключи для обох файлов
    keys_dict_a = set(data_dict_a)
    keys_dict_b = set(data_dict_b)
    dicts_keys = keys_dict_a
    dicts_keys.update(keys_dict_b)

    # отсортировуем полученые ключи
    dicts_keys = sorted(dicts_keys)

    result = check_key_in_dicts(data_dict_a, data_dict_b, dicts_keys)
    return result
