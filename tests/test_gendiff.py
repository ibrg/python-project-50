from gendiff.scripts.generate_diff import generate_diff


file1 = 'tests/fixtures/json/file1.json'
file2 = 'tests/fixtures/json/file2.json'
file3 = 'tests/fixtures/json/file3.json'
file4 = 'tests/fixtures/json/file4.json'



def test_generate_diff():
    with open('tests/fixtures/correct/correct_diff.txt', 'r') as f:
        correct_file = f.read()
    assert correct_file == generate_diff(file1, file2)


def test_stylish_format():
    with open('tests/fixtures/correct/correct_diff.txt', 'r') as f:
        result = f.read()
        assert generate_diff(file1, file2) == result


def test_generate_diff_plain():
    with open('tests/fixtures/correct/correct_plain.txt') as f:
        correct_file = f.read()
        assert correct_file == generate_diff(file3, file4, 'plain')
