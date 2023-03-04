from gendiff.modules.formater import format_result
from gendiff.modules.module import compare
from gendiff.modules.parse import gendiff_args


def main():
    args = gendiff_args()
    print(format_result(compare(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()
