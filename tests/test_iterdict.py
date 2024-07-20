import unittest
from iterdict import ParameterIterator  # Assuming ParameterIterator is a class in your package

class TestParameterIterator(unittest.TestCase):
    def setUp(self):
        self.param_dict = {
            'param1': [1, 2],
            'param2': ['A', 'B']
        }
        self.iterator = ParameterIterator(self.param_dict)

    def test_iteration_count(self):
        """Test if the iterator generates the correct number of combinations."""
        combinations = list(self.iterator)
        expected_combinations = 4  # 2 values in param1 * 2 values in param2
        self.assertEqual(len(combinations), expected_combinations)

    def test_combination_content(self):
        """Test if the combinations generated are correct."""
        combinations = list(self.iterator)
        expected_combinations = [
            {'param1': 1, 'param2': 'A'},
            {'param1': 1, 'param2': 'B'},
            {'param1': 2, 'param2': 'A'},
            {'param1': 2, 'param2': 'B'}
        ]
        self.assertCountEqual(combinations, expected_combinations)

if __name__ == '__main__':
    unittest.main()