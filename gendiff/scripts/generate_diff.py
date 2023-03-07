from gendiff.modules.formater import show_result
from gendiff.modules.module import compare
from gendiff.modules.parse import read_file


def generate_diff(file_path1, file_path2):
    return show_result(compare(read_file(file_path1), read_file(file_path2)))
