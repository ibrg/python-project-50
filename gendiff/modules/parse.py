import argparse
import json
import yaml
from pathlib import Path


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


def read_file(filepath: str) -> dict:
    extension = Path(filepath).suffix
    source = open(filepath)
    if extension == '.json':
        data = json.load(source)
    elif extension == '.yml' or extension == '.yaml':
        data = yaml.safe_load(source)
    else:
        raise('File dosn`t support')
    source.close()
    return data
