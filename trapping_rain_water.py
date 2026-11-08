"""接雨水（Trapping Rain Water）的两种解法。

给定一个长度为 ``n`` 的非负整数数组 ``height``，每个元素表示一根宽度为 1
的柱子的高度，求这些柱子之间总共能接住多少单位的雨水。

例如 ``height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`` 时，答案是 ``6``。

每个位置 ``i`` 上方能积的水量等于
``min(它左侧最高的柱子, 它右侧最高的柱子) - height[i]``（不小于 0）。
两种解法只是求这个量的方式不同：

- :func:`trap`：双指针从两端向中间收缩，始终先处理较矮的一端，
  因此只需要记录左右两侧见过的最大高度。时间复杂度 O(n)，
  额外空间 O(1)，是本题的最优解。
- :func:`trap_with_prefix_max`：先用动态规划分别求出每个位置的
  左侧最大值和右侧最大值，再逐位累加。时间复杂度 O(n)，
  额外空间 O(n)，思路最直观，适合先写出来验证思路。

参考题目：LeetCode 42. Trapping Rain Water
"""

from __future__ import annotations

from typing import Sequence


def trap(height: Sequence[int]) -> int:
    """返回 ``height`` 能接住的雨水总量。

    采用双指针：左右各维护一个指针和“这一侧见过的最大高度”。
    每次移动较矮的一侧，因为该位置能积的水只取决于较矮一侧的最大值。

    >>> trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6
    >>> trap([4, 2, 0, 3, 2, 5])
    9
    """
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


def trap_with_prefix_max(height: Sequence[int]) -> int:
    """用前缀（左）、后缀（右）最大值数组累加，返回雨水总量。

    时间复杂度 O(n)，额外空间 O(n)。

    >>> trap_with_prefix_max([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6
    >>> trap_with_prefix_max([4, 2, 0, 3, 2, 5])
    9
    """
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max = [0] * n
    right_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
