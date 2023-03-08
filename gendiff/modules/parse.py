import argparse
import json
from pathlib import PurePosixPath

import yaml


def gendiff_args():
    parser = argparse.ArgumentParser()
    parser.description = "Compares two configuration \
        files and shows a difference."
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output')
    return parser.parse_args()


def get_file_extension(filepath: str) -> str:
    return PurePosixPath(filepath).suffix


def read_file(filepath: str) -> dict:
    extension = get_file_extension(filepath)
    source = open(filepath)
    if extension == '.json':
        data = json.load(source)
    elif extension in ['.yml', '.yaml']:
        data = yaml.safe_load(source)
    source.close()
    return data
