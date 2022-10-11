import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_string_input(self):
        to_encode = ('Andrey', 'Anastasia', 'Sergey', 'Alena')
        transformed = fit_transform(*to_encode)
        exp_result = [
            ('Andrey', [0, 0, 0, 1]),
            ('Anastasia', [0, 0, 1, 0]),
            ('Sergey', [0, 1, 0, 0]),
            ('Alena', [1, 0, 0, 0])
        ]
        self.assertEqual(transformed, exp_result)

    def test_double_input(self):
        to_encode = ('Andrey', 'Anastasia', 'Andrey')
        transformed = fit_transform(*to_encode)
        exp_result = [
            ('Andrey', [0, 1]),
            ('Anastasia', [1, 0]),
            ('Andrey', [0, 1])
        ]
        self.assertEqual(transformed, exp_result)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_iterable(self):
        to_encode = ('Andrey', 'Anastasia', 'Sergey', 'Alena')
        transformed = fit_transform(to_encode)
        exp_result = [
            ('Andrey', [0, 0, 0, 1]),
            ('Anastasia', [0, 0, 1, 0]),
            ('Sergey', [0, 1, 0, 0]),
            ('Alena', [1, 0, 0, 0])
        ]
        self.assertEqual(transformed, exp_result)

    def test_from_dict(self):
        to_encode = {'Andrey': 1, 'Anastasia': 2, 'Sergey': 3, 'Alena': 4}
        transformed = fit_transform(*to_encode)
        exp_result = [
            ('Andrey', [0, 0, 0, 1]),
            ('Anastasia', [0, 0, 1, 0]),
            ('Sergey', [0, 1, 0, 0]),
            ('Alena', [1, 0, 0, 0])
        ]
        for result, right_answer in zip(transformed, exp_result):
            self.assertTupleEqual(result, right_answer)