# superagent_test

用于演示 Superagent 的测试仓库

## 快速排序

`quicksort.py` 实现了快速排序（平均 O(n log n)，三数取中选基准，原地划分）：

```python
from quicksort import quicksort

print(quicksort([5, 2, 9, 1, 5]))  # [1, 2, 5, 5, 9]
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
