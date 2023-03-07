from gendiff.modules.formater import stylish_format, json_format
from gendiff.modules.module import compare
from gendiff.modules.parse import read_file


FORMATS = {
    "stylish": stylish_format,
    "json": json_format
}


def generate_diff(file_path1, file_path2, type_format="stylish"):
    format = FORMATS[type_format]
    return format(compare(read_file(file_path1), read_file(file_path2)))
