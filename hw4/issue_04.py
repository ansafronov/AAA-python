import pytest
from one_hot_encoder import fit_transform


def test_strings_input():
    to_encode = ('Andrey', 'Anastasia', 'Sergey', 'Alena')
    transformed = fit_transform(*to_encode)
    exp_result = [
        ('Andrey', [0, 0, 0, 1]),
        ('Anastasia', [0, 0, 1, 0]),
        ('Sergey', [0, 1, 0, 0]),
        ('Alena', [1, 0, 0, 0])
    ]
    assert transformed == exp_result


def test_from_dict():
    to_encode = {'Andrey': 1, 'Anastasia': 2, 'Sergey': 3, 'Alena': 4}
    transformed = fit_transform(to_encode)
    exp_result = [
        ('Andrey', [0, 0, 0, 1]),
        ('Anastasia', [0, 0, 1, 0]),
        ('Sergey', [0, 1, 0, 0]),
        ('Alena', [1, 0, 0, 0])
    ]
    assert transformed == exp_result


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_double():
    to_encode = ('Andrey', 'Andrey')
    transformed = fit_transform(*to_encode)
    exp_result = [
        ('Andrey', [1]),
        ('Andrey', [1])
    ]
    assert transformed == exp_result

def test_case_sensitive():
    to_encode = ('ANDREY', 'andrey')
    transformed = fit_transform(*to_encode)
    exp_result = [
        ('ANDREY', [0, 1]),
        ('andrey', [1, 0])
    ]
    assert transformed == exp_result

def test_one_input():
    input_string = 'Andrey'
    to_encode = (input_string)
    transformed = fit_transform(*to_encode)
    assert len(transformed) == 6

    input_length = len(input_string)
    for i, (letter, code) in enumerate(transformed):
        assert letter == input_string[i]
        assert code == [0 if j != i else 1 for j, _ in zip(range(input_length-1, -1, -1), input_string)]
