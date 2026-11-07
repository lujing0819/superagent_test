"""quicksort.py 的测试。运行：python3 -m unittest -v"""

import random
import unittest

from quicksort import quicksort


class QuicksortTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(quicksort([]), [])

    def test_single(self):
        self.assertEqual(quicksort([42]), [42])

    def test_sorted(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(quicksort([2, 2, 1, 2, 1, 3]), [1, 1, 2, 2, 2, 3])

    def test_all_equal(self):
        self.assertEqual(quicksort([7] * 20), [7] * 20)

    def test_negative_and_float(self):
        self.assertEqual(quicksort([0.5, -1, 3, -2.5]), [-2.5, -1, 0.5, 3])

    def test_strings(self):
        self.assertEqual(quicksort(["pear", "apple", "fig"]), ["apple", "fig", "pear"])

    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        quicksort(data)
        self.assertEqual(data, [3, 1, 2])

    def test_accepts_tuple_and_generator(self):
        self.assertEqual(quicksort((3, 1, 2)), [1, 2, 3])
        self.assertEqual(quicksort(x for x in [3, 1, 2]), [1, 2, 3])

    def test_matches_sorted_on_random_data(self):
        rng = random.Random(20261107)
        for _ in range(50):
            data = [rng.randint(-1000, 1000) for _ in range(rng.randint(0, 300))]
            self.assertEqual(quicksort(data), sorted(data))

    def test_large_random(self):
        rng = random.Random(1)
        data = [rng.random() for _ in range(10000)]
        self.assertEqual(quicksort(data), sorted(data))


if __name__ == "__main__":
    unittest.main()
