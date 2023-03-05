import json
from gendiff.modules.formater import format_result
from gendiff.modules.module import compare
from gendiff.modules.parse import get_file_extension


file1 = 'tests/fixtures/json/file1.json'
file2 = 'tests/fixtures/json/file2.json'
file3 = 'tests/fixtures/json/file3.json'
file4 = 'tests/fixtures/json/file4.json'
file5 = 'tests/fixtures/yaml/file1.yml'
file6 = 'tests/fixtures/yaml/file3.yaml'


correct_file = open('tests/fixtures/correct/correct_diff.txt', 'r')
correct_file = correct_file.read()

correct_json = json.dumps(json.load(open('tests/fixtures/correct/correct_json.json')), indent=4)


def test_generate_diff():
    result = format_result(compare(file1, file2))
    assert correct_file == result


def test_get_file_extension():
    result_json = get_file_extension(file1)
    result_yml = get_file_extension(file5)
    result_yaml = get_file_extension(file6)

    excepted_json = '.json'
    excepted_yml = '.yml'
    excepted_yaml = '.yaml'
    excepted_txt = '.txt'
    assert excepted_json == result_json
    assert excepted_yml == result_yml
    assert excepted_yaml == result_yaml
    assert excepted_txt != result_json
    