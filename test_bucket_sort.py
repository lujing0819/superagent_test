"""bucket_sort.py 的测试。运行：python3 -m unittest -v"""

import random
import unittest

from bucket_sort import bucket_sort


class BucketSortTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(bucket_sort([]), [])

    def test_single(self):
        self.assertEqual(bucket_sort([42]), [42])

    def test_sorted(self):
        self.assertEqual(bucket_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(bucket_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(bucket_sort([2, 2, 1, 2, 1, 3]), [1, 1, 2, 2, 2, 3])

    def test_all_equal(self):
        self.assertEqual(bucket_sort([7] * 20), [7] * 20)

    def test_negative_and_float(self):
        self.assertEqual(bucket_sort([0.5, -1, 3, -2.5]), [-2.5, -1, 0.5, 3])

    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        bucket_sort(data)
        self.assertEqual(data, [3, 1, 2])

    def test_accepts_tuple_and_generator(self):
        self.assertEqual(bucket_sort((3, 1, 2)), [1, 2, 3])
        self.assertEqual(bucket_sort(x for x in [3, 1, 2]), [1, 2, 3])

    def test_custom_bucket_count(self):
        data = [5, 2, 9, 1, 5]
        for count in (1, 2, 5, 100):
            with self.subTest(bucket_count=count):
                self.assertEqual(bucket_sort(data, bucket_count=count), [1, 2, 5, 5, 9])

    def test_invalid_bucket_count(self):
        with self.assertRaises(ValueError):
            bucket_sort([1, 2], bucket_count=0)
        with self.assertRaises(ValueError):
            bucket_sort([1, 2], bucket_count=-3)

    def test_matches_sorted_on_random_ints(self):
        rng = random.Random(20261108)
        for _ in range(50):
            data = [rng.randint(-1000, 1000) for _ in range(rng.randint(0, 300))]
            self.assertEqual(bucket_sort(data), sorted(data))

    def test_matches_sorted_on_skewed_data(self):
        rng = random.Random(7)
        data = [rng.random() ** 3 for _ in range(2000)]
        self.assertEqual(bucket_sort(data), sorted(data))

    def test_large_random(self):
        rng = random.Random(1)
        data = [rng.random() for _ in range(10000)]
        self.assertEqual(bucket_sort(data), sorted(data))


if __name__ == "__main__":
    unittest.main()
