# import json
# from gendiff.scripts.generate_diff import generate_diff
# from gendiff.modules.parse import read_file
# from gendiff.format.stylish import stylish_format
# from gendiff.format.plain import plain_format


# file1 = 'tests/fixtures/json/file1.json'
# file2 = 'tests/fixtures/json/file2.json'
# file3 = 'tests/fixtures/json/file3.json'
# file4 = 'tests/fixtures/json/file4.json'
# file5 = 'tests/fixtures/yaml/file1.yml'
# file6 = 'tests/fixtures/yaml/file3.yaml'

# correct_file = open('tests/fixtures/correct/correct_diff.txt', 'r')
# correct_file = correct_file.read()

# correct_json = json.dumps(json.load(open('tests/fixtures/correct/correct_json.json')), indent=4)


# def test_generate_diff():
#     dict1 = read_file(file3)
#     dict2 = read_file(file4)
#     result = plain_format(generate_diff(dict1, dict2))
#     assert correct_file == result


import json
from gendiff.format.stylish import stylish_format
from gendiff.modules.module import compare
from gendiff.modules.parse import  read_file
from gendiff.scripts.generate_diff import generate_diff


file1 = 'tests/fixtures/json/file1.json'
file2 = 'tests/fixtures/json/file2.json'
file3 = 'tests/fixtures/json/file3.json'
file4 = 'tests/fixtures/json/file4.json'



def test_generate_diff():
    with  open('tests/fixtures/correct/correct_diff.txt', 'r') as f:
        correct_file = f.read()
    assert correct_file == generate_diff(file1, file2)
       

def test_generate_diff_stylish():
    with open('tests/fixtures/correct/correct_stylish.txt') as f:
        correct_file = f.read()
        assert correct_file == generate_diff(file3, file4)


def test_generate_diff_plain():
    with open('tests/fixtures/correct/correct_plain.txt') as f:
        correct_file = f.read()
        assert correct_file == generate_diff(file3, file4, 'plain')
