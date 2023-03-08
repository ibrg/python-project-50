from gendiff.format import json, plain, stylish
from gendiff.modules.module import compare
from gendiff.modules.parse import read_file


FORMATS = {
    "stylish": stylish.stylish_format,
    "json": json.json_format,
    "plain": plain.plain_format
}


def generate_diff(file_path1, file_path2, format="stylish"):
    type_format = FORMATS[format]
    return type_format(compare(read_file(file_path1), read_file(file_path2)))
