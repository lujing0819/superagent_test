"""桶排序（Bucket sort）的 Python 实现。

桶排序先求出序列的最小值和最大值，把整个数值范围均匀划分为若干个桶，
按元素大小把它放进对应的桶里；每个桶内部用插入排序排好，最后再按桶的
顺序把结果拼接起来。

桶排序适合数值范围已知且分布比较均匀的数据：此时每个桶里只有很少的
元素，平均时间复杂度接近 O(n)。如果数据都挤在少数几个桶里，桶内的插入
排序就会退化，最坏时间复杂度为 O(n^2)，所以它不像快速排序那样有稳定的
O(n log n) 保证。

性能：
- 平均时间复杂度 O(n)（分布均匀、桶数取元素个数时）
- 最坏时间复杂度 O(n^2)（分布极不均匀）
- 额外空间 O(n)，用来存放各个桶

桶内使用插入排序，相等元素的相对顺序不会改变，因此桶排序是稳定的。
"""

from __future__ import annotations

from typing import Iterable, List, Optional, TypeVar

T = TypeVar("T")


def bucket_sort(items: Iterable[T], bucket_count: Optional[int] = None) -> List[T]:
    """返回 ``items`` 升序排序后的新列表。

    传入的可迭代对象不会被修改。元素必须是支持比较、减法和除法的数值
    （例如 int、float）。

    ``bucket_count`` 指定桶的数量，默认等于元素个数；数据在数值范围上
    分布得越均匀，这个默认值的效果越好。所有元素相等时直接返回，不需要
    划分桶。

    >>> bucket_sort([0.42, 0.13, 0.97, 0.05])
    [0.05, 0.13, 0.42, 0.97]
    >>> bucket_sort([3, 1, 2], bucket_count=3)
    [1, 2, 3]
    """
    if bucket_count is not None and bucket_count < 1:
        raise ValueError("bucket_count 必须大于 0")

    values = list(items)
    n = len(values)
    if n < 2:
        return values

    lo = min(values)
    hi = max(values)
    if lo == hi:
        return values

    if bucket_count is None:
        bucket_count = n

    width = (hi - lo) / bucket_count
    buckets: List[List[T]] = [[] for _ in range(bucket_count)]
    for value in values:
        index = int((value - lo) / width)
        # value 恰好等于最大值时，浮点误差可能让下标算成桶数，收回到最后一个桶。
        if index >= bucket_count:
            index = bucket_count - 1
        buckets[index].append(value)

    result: List[T] = []
    for bucket in buckets:
        _insertion_sort(bucket)
        result.extend(bucket)
    return result


def _insertion_sort(a: List[T]) -> None:
    """原地把 ``a`` 升序排序；桶内元素很少，插入排序足够快。"""
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and current < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current


if __name__ == "__main__":
    print(bucket_sort([3, 6, 8, 10, 1, 2, 1]))
