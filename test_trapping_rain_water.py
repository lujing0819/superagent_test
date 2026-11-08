"""trapping_rain_water.py 的测试。运行：python3 -m unittest -v"""

import random
import unittest

from trapping_rain_water import trap, trap_with_prefix_max


def brute_force(height):
    """逐个位置求出左右最高柱子的朴素解，用于对照验证。"""
    water = 0
    for i in range(len(height)):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])
        water += min(left_max, right_max) - height[i]
    return water


class TrappingRainWaterTests(unittest.TestCase):
    def test_leetcode_example(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_second_example(self):
        self.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9)

    def test_empty(self):
        self.assertEqual(trap([]), 0)

    def test_single(self):
        self.assertEqual(trap([42]), 0)

    def test_two(self):
        self.assertEqual(trap([5, 1]), 0)

    def test_no_water(self):
        self.assertEqual(trap([1, 2, 3, 4, 5]), 0)
        self.assertEqual(trap([5, 4, 3, 2, 1]), 0)
        self.assertEqual(trap([3, 3, 3, 3]), 0)

    def test_valleys(self):
        self.assertEqual(trap([2, 0, 2]), 2)
        self.assertEqual(trap([3, 0, 0, 3]), 6)
        self.assertEqual(trap([5, 2, 3, 2, 5]), 8)

    def test_does_not_mutate_input(self):
        data = [2, 0, 2]
        trap(data)
        self.assertEqual(data, [2, 0, 2])

    def test_accepts_tuple(self):
        self.assertEqual(trap((0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)), 6)

    def test_prefix_max_matches_examples(self):
        self.assertEqual(trap_with_prefix_max([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap_with_prefix_max([4, 2, 0, 3, 2, 5]), 9)
        self.assertEqual(trap_with_prefix_max([]), 0)
        self.assertEqual(trap_with_prefix_max([5, 4, 3, 2, 1]), 0)

    def test_both_implementations_match_brute_force(self):
        rng = random.Random(42)
        for _ in range(200):
            n = rng.randint(0, 30)
            height = [rng.randint(0, 10) for _ in range(n)]
            expected = brute_force(height)
            self.assertEqual(trap(height), expected)
            self.assertEqual(trap_with_prefix_max(height), expected)

    def test_large_input(self):
        rng = random.Random(1)
        height = [rng.randint(0, 10**6) for _ in range(20000)]
        self.assertEqual(trap(height), trap_with_prefix_max(height))


if __name__ == "__main__":
    unittest.main()
