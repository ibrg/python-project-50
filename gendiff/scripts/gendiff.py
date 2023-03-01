import argparse
from ..modules.generate import generate_diff


def gendiff_help():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    file1 = args.first_file
    file2 = args.second_file

    diff = generate_diff(file1, file2)

    return diff


def main():
    gendiff_help()


if __name__ == '__main__':
    main()
