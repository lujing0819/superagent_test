# superagent_test

用于演示 Superagent 的测试仓库

## 快速排序

`quicksort.py` 实现了快速排序（平均 O(n log n)，三数取中选基准，原地划分）：

```python
from quicksort import quicksort

print(quicksort([5, 2, 9, 1, 5]))  # [1, 2, 5, 5, 9]
```

运行测试：`python3 -m unittest -v`

## 桶排序

`bucket_sort.py` 实现了桶排序（数据分布均匀时期望 O(n)，桶内用插入排序）：

```python
from bucket_sort import bucket_sort

print(bucket_sort([0.42, 0.13, 0.97, 0.05]))  # [0.05, 0.13, 0.42, 0.97]
```

运行测试：`python3 -m unittest -v`

## 八皇后

`eight_queens.py` 用回溯法求解八皇后问题，返回全部 92 个解：

```python
from eight_queens import format_solution, solve_n_queens

solutions = solve_n_queens(8)
print(len(solutions))  # 92
print(format_solution(solutions[0]))
```

运行测试：`python3 -m unittest -v`

## 接雨水

`trapping_rain_water.py` 实现 LeetCode 42 接雨水的两种解法：双指针（O(n) 时间、O(1) 额外空间）和
前缀最大值（O(n) 时间、O(n) 额外空间）：

```python
from trapping_rain_water import trap

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
```

运行测试：`python3 -m unittest -v`
