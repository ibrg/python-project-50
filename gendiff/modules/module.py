import json


UNCHANGE = ' '  # ключ есть в обоих файлах
REMOVE = '-'  # находится в первом файле
ADDED = '+'  # находится во втором файле


def read_file(file, type=json):
    with open(file) as f:
        file = json.load(f)
    return file


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


def format_result(data: dict, type_format='json') -> str:
    # Форматируем вывод согласно формату (по умолчанию json)
    # Пример отображения
    """
        {
        - follow: false
            host: hexlet.io
        - timeout: 50
        + timeout: 20
        + verbose: true
        }
    """
    show = []
    if type_format == 'json':
        show = [f" {k} {v['value']}\n" for k, v in data.items()]
    print('{\n', *show, '}')


def compare(file1, file2):
    # TODO: нужно добавить поддержку файлов yaml
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
    return format_result(result)
