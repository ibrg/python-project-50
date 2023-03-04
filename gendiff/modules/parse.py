import argparse
import json


def gendiff_args():
    parser = argparse.ArgumentParser()
    parser.description = \
        "Compares two configuration files and shows a difference."
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def read_file(file):
    with open(file) as f:
        file = json.load(f)
    return file
