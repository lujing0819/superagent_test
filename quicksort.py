"""快速排序（Quicksort）的 Python 实现。

快速排序采用分治思想：先选一个基准值（pivot），把序列划分成小于基准和
不小于基准的两部分，再对两部分分别递归排序。

性能：
- 平均时间复杂度 O(n log n)
- 最坏时间复杂度 O(n^2)（这里用三数取中降低有序输入退化到最坏情况的概率）
- 额外空间 O(log n)，来自递归栈
"""

from __future__ import annotations

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def quicksort(items: Iterable[T]) -> List[T]:
    """返回 ``items`` 升序排序后的新列表。

    传入的可迭代对象不会被修改；元素只需要支持 ``<`` 比较。

    >>> quicksort([3, 1, 2])
    [1, 2, 3]
    """
    result = list(items)
    _quicksort(result, 0, len(result) - 1)
    return result


def _quicksort(a: List[T], lo: int, hi: int) -> None:
    """原地排序 ``a[lo:hi + 1]``。"""
    while lo < hi:
        pivot_index = _partition(a, lo, hi)
        # 先递归较短的一侧，较长的一侧用循环处理，
        # 递归深度因此保持在 O(log n)，避免大规模有序输入导致栈溢出。
        if pivot_index - lo < hi - pivot_index:
            _quicksort(a, lo, pivot_index - 1)
            lo = pivot_index + 1
        else:
            _quicksort(a, pivot_index + 1, hi)
            hi = pivot_index - 1


def _partition(a: List[T], lo: int, hi: int) -> int:
    """用三数取中选基准做划分，返回基准元素最终所在的下标。"""
    mid = (lo + hi) // 2
    # 三次比较之后满足 a[lo] <= a[mid] <= a[hi]。
    if a[mid] < a[lo]:
        a[mid], a[lo] = a[lo], a[mid]
    if a[hi] < a[lo]:
        a[hi], a[lo] = a[lo], a[hi]
    if a[hi] < a[mid]:
        a[hi], a[mid] = a[mid], a[hi]
    # 把中位数换到末尾作为基准，然后做 Lomuto 划分。
    a[mid], a[hi] = a[hi], a[mid]

    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


if __name__ == "__main__":
    print(quicksort([3, 6, 8, 10, 1, 2, 1]))
