import unittest
from collections import OrderedDict
from lib.combination_picker import CombinationPicker


class TestCombinationPicker(unittest.TestCase):
    def setUp(self):
        self.candidates = OrderedDict([
            ('color', ['red', 'green', 'blue']),
            ('size', ['small', 'medium', 'large', 'xl']),
            ('shape', ['circle', 'square'])
        ])
        self.picker = CombinationPicker(self.candidates)

    def test_all_combination_counts(self):
        expected_combinations = 3 * 4 * 2  # 3 colors, 4 sizes, 2 shapes
        self.assertEqual(
            self.picker.all_combination_counts,
            expected_combinations
        )

    def test_pick_combination(self):
        expected = [
            {'color': 'red', 'size': 'small', 'shape': 'circle'},
            {'color': 'green', 'size': 'small', 'shape': 'circle'},
            {'color': 'blue', 'size': 'small', 'shape': 'circle'},

            {'color': 'red', 'size': 'medium', 'shape': 'circle'},
            {'color': 'green', 'size': 'medium', 'shape': 'circle'},
            {'color': 'blue', 'size': 'medium', 'shape': 'circle'},

            {'color': 'red', 'size': 'large', 'shape': 'circle'},
            {'color': 'green', 'size': 'large', 'shape': 'circle'},
            {'color': 'blue', 'size': 'large', 'shape': 'circle'},

            {'color': 'red', 'size': 'xl', 'shape': 'circle'},
            {'color': 'green', 'size': 'xl', 'shape': 'circle'},
            {'color': 'blue', 'size': 'xl', 'shape': 'circle'},

            {'color': 'red', 'size': 'small', 'shape': 'square'},
            {'color': 'green', 'size': 'small', 'shape': 'square'},
            {'color': 'blue', 'size': 'small', 'shape': 'square'},

            {'color': 'red', 'size': 'medium', 'shape': 'square'},
            {'color': 'green', 'size': 'medium', 'shape': 'square'},
            {'color': 'blue', 'size': 'medium', 'shape': 'square'},

            {'color': 'red', 'size': 'large', 'shape': 'square'},
            {'color': 'green', 'size': 'large', 'shape': 'square'},
            {'color': 'blue', 'size': 'large', 'shape': 'square'},

            {'color': 'red', 'size': 'xl', 'shape': 'square'},
            {'color': 'green', 'size': 'xl', 'shape': 'square'},
            {'color': 'blue', 'size': 'xl', 'shape': 'square'},
        ]

        for i in range(len(expected)):
            self.assertDictEqual(
                self.picker.pick_combination(i),
                expected[i]
            )

        self.assertEqual(self.picker.all_combination_counts - 1, i)

    def test_pick_combination_exception(self):
        try:
            self.picker.pick_combination(self.picker.all_combination_counts)
        except ValueError as e:
            self.assertEqual(str(e), "Index out of range")


if __name__ == '__main__':
    unittest.main()
