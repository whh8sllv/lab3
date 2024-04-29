from main import BubbleSort, QuickSort, Sorter
import unittest


class TestStrategy(unittest.TestCase):
    def test_bubble_empty_list(self):
        self.assertEqual(Sorter(BubbleSort()).sort_data([]), [])

    def test_quick_empty_list(self):
        self.assertEqual(Sorter(QuickSort()).sort_data([]), [])

    def test_single_element_bubble_list(self):
        self.assertEqual(Sorter(BubbleSort()).sort_data([3]), [3])

    def test_single_element_quick_list(self):
        self.assertEqual(Sorter(QuickSort()).sort_data([1]), [1])

    def test_same_elements_bubble_list(self):
        self.assertEqual(Sorter(BubbleSort()).sort_data([0, 1, 2, 0]), [0, 0, 1, 2])

    def test_same_elements_quick_list(self):
        self.assertEqual(Sorter(QuickSort()).sort_data([2, 8, 2, 9]), [2, 2, 8, 9])

    def test_negative_elements_bubble_list(self):
        self.assertEqual(Sorter(BubbleSort()).sort_data([-1, 6, 8, -5]), [-5, -1, 6, 8])

    def test_negative_elements_quick_list(self):
        self.assertEqual(Sorter(QuickSort()).sort_data([0, -18, 10, -7]), [-18, -7, 0, 10])

    def test_default_bubble_list(self):
        self.assertEqual(Sorter(BubbleSort()).sort_data([-12, 13.4, 0, 14.4, 1, -1, 1]), [-12, -1, 0, 1, 1, 13.4, 14.4])

    def test_default_quick_list(self):
        self.assertEqual(Sorter(QuickSort()).sort_data([-1, 0, -88, 1.6, 3, 2, 100, 12]), [-88, -1, 0, 1.6, 2, 3, 12, 100])


if __name__ == '__main__':
    unittest.main()