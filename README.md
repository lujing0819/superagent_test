# superagent_test

用于演示 Superagent 的测试仓库

## 快速排序

`quicksort.py` 实现了快速排序（平均 O(n log n)，三数取中选基准，原地划分）：

```python
from quicksort import quicksort

print(quicksort([5, 2, 9, 1, 5]))  # [1, 2, 5, 5, 9]
```

运行测试：`python3 -m unittest -v`

## 冒泡排序

`bubble_sort.py` 实现了冒泡排序（平均 O(n²)，原地交换，已有序时提前结束）：

```python
from bubble_sort import bubble_sort

print(bubble_sort([5, 2, 9, 1, 5]))  # [1, 2, 5, 5, 9]
```

运行测试：`python3 -m unittest -v`
