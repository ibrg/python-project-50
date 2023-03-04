import pytest
import json
from gendiff.modules.module import compare
from gendiff.modules.formater import format_result


file1 = 'tests/fixtures/json/file1.json'
file2 = 'tests/fixtures/json/file2.json'


correct_file = open('tests/fixtures/correct/correct_diff.txt', 'r')
correct_file = correct_file.read()


def test_generate_diff():
    result = format_result(compare(file1, file2))
    assert correct_file == result
