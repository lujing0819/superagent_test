"""冒泡排序（Bubble Sort）的 Python 实现。

每一轮从头到尾比较相邻的两个元素，前一个比后一个大就交换它们。
一轮结束后，本轮最大的元素会“冒泡”到未排序部分的末尾。
如果某一轮没有发生任何交换，说明序列已经有序，可以提前结束。

性能：
- 平均时间复杂度 O(n^2)
- 最坏时间复杂度 O(n^2)
- 最好时间复杂度 O(n)（已经有序时只扫描一轮）
- 额外空间 O(1)，排序在列表副本上原地进行
"""

from __future__ import annotations

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def bubble_sort(items: Iterable[T]) -> List[T]:
    """返回 ``items`` 升序排序后的新列表。

    传入的可迭代对象不会被修改；元素只需要支持 ``<`` 比较。

    >>> bubble_sort([3, 1, 2])
    [1, 2, 3]
    """
    result = list(items)
    n = len(result)
    # 每轮把当前未排序部分的最大值放到末尾，末尾已排好的元素不用再比较。
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i + 1] < result[i]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    print(bubble_sort([3, 6, 8, 10, 1, 2, 1]))
