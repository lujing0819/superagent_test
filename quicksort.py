"""快速排序（Quicksort）的 Python 实现。

快速排序采用分治思想，整个过程可以概括为三步：

1. 选择基准：从待排序区间中挑一个元素作为基准值（pivot）；
2. 划分：把区间里的元素重新排列成“小于基准”和“不小于基准”两部分，
   基准值最终落在两部分的交界处；
3. 递归：对基准左右两侧的子区间重复第 1、2 步，直到子区间为空或只剩
   一个元素，此时整个区间就有序了。

这里实现的是原地（in-place）排序：只有对外接口 :func:`quicksort` 会把
输入复制成列表，之后的比较和交换都直接在这个列表内部进行，因此不会
修改调用方传入的可迭代对象。

性能：
- 平均时间复杂度 O(n log n)
- 最坏时间复杂度 O(n^2)（这里用三数取中降低有序输入退化到最坏情况的概率）
- 额外空间 O(log n)，来自递归栈

注意：快速排序是不稳定排序，值相等的元素在排序后相对顺序可能改变。
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
    # 转成列表有两个作用：一是复制输入、保护调用方的数据，
    # 二是让后续可以用下标和交换操作做原地排序。
    result = list(items)
    _quicksort(result, 0, len(result) - 1)
    return result


def _quicksort(a: List[T], lo: int, hi: int) -> None:
    """原地排序闭区间 ``a[lo:hi + 1]``（``hi`` 是最后一个元素的下标）。"""
    # 用 while 循环处理“较长的一侧”，只对较短的一侧递归：
    # 每一轮划分后，较短一侧的长度不超过当前区间的一半，
    # 因此递归深度始终是 O(log n)，大规模有序输入也不会栈溢出。
    while lo < hi:
        # 划分后基准元素落在 pivot_index，且它左侧都小于基准、右侧都不小于基准。
        pivot_index = _partition(a, lo, hi)
        if pivot_index - lo < hi - pivot_index:
            # 左半部分更短：递归排序左边，右边交给下一轮循环。
            _quicksort(a, lo, pivot_index - 1)
            lo = pivot_index + 1
        else:
            # 右半部分更短（或两边等长）：递归排序右边，左边交给下一轮循环。
            _quicksort(a, pivot_index + 1, hi)
            hi = pivot_index - 1


def _partition(a: List[T], lo: int, hi: int) -> int:
    """用三数取中选基准做划分，返回基准元素最终所在的下标。

    划分完成后，``a[lo:pivot_index]`` 中的元素都小于基准，
    ``a[pivot_index + 1:hi + 1]`` 中的元素都不小于基准。
    """
    mid = (lo + hi) // 2
    # 第一步：把 a[lo]、a[mid]、a[hi] 三个数调整为有序。
    # 连续三次比较交换后，一定有 a[lo] <= a[mid] <= a[hi]。
    if a[mid] < a[lo]:
        a[mid], a[lo] = a[lo], a[mid]  # 让 a[lo] <= a[mid]
    if a[hi] < a[lo]:
        a[hi], a[lo] = a[lo], a[hi]  # 让 a[lo] 成为三者中的最小值
    if a[hi] < a[mid]:
        a[hi], a[mid] = a[mid], a[hi]  # 让 a[mid] <= a[hi]
    # 此时 a[mid] 是三数中的中位数。对已经有序的输入，中位数比固定取首元素
    # 更能把区间均分，避免划分退化成每次只缩小一个元素。
    # 把它换到区间末尾 a[hi] 暂存，作为划分基准。
    a[mid], a[hi] = a[hi], a[mid]

    pivot = a[hi]
    # 第二步：Lomuto 划分。扫描过程中始终维护以下循环不变量
    # （j 是当前扫描位置，a[hi] 是基准本身）：
    # - a[lo:i]  里的元素都小于 pivot；
    # - a[i:j]   里的元素都不小于 pivot；
    # - a[j:hi]  是尚未检查的元素。
    i = lo  # i 指向“小于 pivot 的区域”之后的下一个空位
    for j in range(lo, hi):
        if a[j] < pivot:
            # 当前元素小于基准：把它换到“小于 pivot”区域的末尾，区域扩大一格。
            a[i], a[j] = a[j], a[i]
            i += 1
    # 第三步：基准还暂存在 a[hi]，把它换到两部分中间。
    # 交换后，i 左侧的元素全部小于 pivot，i 右侧（不含 i）全部不小于 pivot。
    a[i], a[hi] = a[hi], a[i]
    return i


if __name__ == "__main__":
    print(quicksort([3, 6, 8, 10, 1, 2, 1]))
