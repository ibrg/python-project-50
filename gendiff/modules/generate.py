import json


def sort_dict_by_keys(dict):
    dict_keys = list(dict.keys())
    dict_keys.sort()
    sorted_dict = {k: dict[k] for k in dict_keys}
    return sorted_dict


def compare(file1, file2):
    # len file1 >= file2
    result = '{\n'
    # sorting file1
    sorted_file1 = sort_dict_by_keys(file1)
    sorted_file2 = sort_dict_by_keys(file2)

    for k, v in sorted_file1.items():
        if not file2.get(k):
            result += f'- {k}: {v} \n'

        elif file2.get(k) != v:
            result += f'- {k}: {v} \n'
            result += f"+ {k}: {file2.get(k)}\n"
            
        elif k in file2 and v == file2.get(k):
            result += f"  {k}: {file2.get(k)}\n"
        else:
            result += f"+ {k}: {v}"

    for k, v in sorted_file2.items():
        if k not in file1:
            result += f"+ {k}: {v}"

    result += '\n}'
    return result


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    if len(file2) > len(file1):
        print(compare(file2, file1))
        return
    print(compare(file1, file2))
