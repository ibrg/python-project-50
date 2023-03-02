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
    data_dict_a = read_file(file1)
    data_dict_b = read_file(file2)  # TODO: нужно добавить поддержку файлов yaml

    # Находим уникальные ключи для обох файлов
    keys_dict_a = set(data_dict_a)
    keys_dict_b = set(data_dict_b)
    dicts_keys = keys_dict_a
    dicts_keys.update(keys_dict_b)

    # отсортировуем полученые ключи
    dicts_keys = sorted(dicts_keys)

    result = check_key_in_dicts(data_dict_a, data_dict_b, dicts_keys)
    return format_result(result)


# def sort_dict_by_keys(dict):
#     dict_keys = list(dict.keys())
#     dict_keys.sort()
#     sorted_dict = {k: dict[k] for k in dict_keys}
#     return sorted_dict


# def compare(file1, file2):
#     # len file1 >= file2
#     result = '{\n'
#     # sorting file1
#     sorted_file1 = sort_dict_by_keys(file1)
#     sorted_file2 = sort_dict_by_keys(file2)

#     for k, v in sorted_file1.items():
#         if not file2.get(k):
#             result += f'- {k}: {v} \n'
#         elif file2.get(k) != v:
#             result += f'- {k}: {v} \n'
#             result += f"+ {k}: {file2.get(k)}\n"
#         elif k in file2 and v == file2.get(k):
#             result += f"  {k}: {file2.get(k)}\n"
#         else:
#             result += f"+ {k}: {v}"

#     for k, v in sorted_file2.items():
#         if k not in file1:
#             result += f"+ {k}: {v}"

#     result += '\n}'
#     return result


# def generate_diff(file_path1, file_path2):
#     file1 = json.load(open(file_path1))
#     file2 = json.load(open(file_path2))

#     if len(file2) > len(file1):
#         print(compare(file2, file1))
#         return
#     print(compare(file1, file2))
