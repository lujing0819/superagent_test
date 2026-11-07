"""bubble_sort.py 的测试。运行：python3 -m unittest -v"""

import random
import unittest

from bubble_sort import bubble_sort


class BubbleSortTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(bubble_sort([2, 2, 1, 2, 1, 3]), [1, 1, 2, 2, 2, 3])

    def test_all_equal(self):
        self.assertEqual(bubble_sort([7] * 20), [7] * 20)

    def test_negative_and_float(self):
        self.assertEqual(bubble_sort([0.5, -1, 3, -2.5]), [-2.5, -1, 0.5, 3])

    def test_strings(self):
        self.assertEqual(bubble_sort(["pear", "apple", "fig"]), ["apple", "fig", "pear"])

    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        bubble_sort(data)
        self.assertEqual(data, [3, 1, 2])

    def test_accepts_tuple_and_generator(self):
        self.assertEqual(bubble_sort((3, 1, 2)), [1, 2, 3])
        self.assertEqual(bubble_sort(x for x in [3, 1, 2]), [1, 2, 3])

    def test_matches_sorted_on_random_data(self):
        rng = random.Random(20261107)
        for _ in range(50):
            data = [rng.randint(-1000, 1000) for _ in range(rng.randint(0, 300))]
            self.assertEqual(bubble_sort(data), sorted(data))

    def test_stops_early_on_sorted_input(self):
        # 已有序时，比较次数应只有一轮，而不是 O(n^2)。
        class Noisy(int):
            comparisons = 0

            def __lt__(self, other):
                Noisy.comparisons += 1
                return int.__lt__(self, other)

        data = [Noisy(i) for i in range(50)]
        bubble_sort(data)
        self.assertEqual(Noisy.comparisons, 49)


if __name__ == "__main__":
    unittest.main()
