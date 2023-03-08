from gendiff.modules.parse import gendiff_args
from gendiff.scripts.generate_diff import generate_diff


def main():
    args = gendiff_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
