from gendiff.modules.parse import gendiff_args
from gendiff.modules.module import compare
from gendiff.modules.formater import show_result


def main():
    args = gendiff_args()
    show_result(compare(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
