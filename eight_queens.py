"""八皇后（Eight Queens）的 Python 实现。

八皇后问题要求在 8×8 的棋盘上摆放 8 个皇后，使任意两个皇后都不在
同一行、同一列或同一条斜线上。这里用回溯法找出全部解，也可以求解
任意 n×n 棋盘上的 n 皇后问题。

每个解用一个长度为 n 的列表表示：列表第 row 个元素是第 row 行皇后
所在的列号（行列都从 0 开始）。

性能：八个皇后的全部 92 个解可以很快枚举完，回溯过程中用集合记录
已经占用的列和斜线，单步判断为 O(1)。
"""

from __future__ import annotations

from typing import List


def solve_n_queens(n: int = 8) -> List[List[int]]:
    """返回 n 皇后问题的所有解。

    参数 ``n`` 必须是正整数。返回值中每个解都是一个列号列表，例如
    ``[1, 3, 0, 2]`` 表示第 0 行的皇后在第 1 列，第 1 行的皇后在第
    3 列，依此类推。默认求解经典的八皇后问题，共有 92 个解。

    >>> len(solve_n_queens(8))
    92
    >>> solve_n_queens(2)
    []
    """
    if n < 1:
        raise ValueError("n 必须是正整数")

    solutions: List[List[int]] = []
    placement: List[int] = []
    occupied_columns = set()
    occupied_diagonals_down = set()  # row - col 相同的格子在一条斜线上
    occupied_diagonals_up = set()  # row + col 相同的格子在另一条斜线上

    def backtrack(row: int) -> None:
        if row == n:
            solutions.append(placement.copy())
            return

        for column in range(n):
            if (
                column in occupied_columns
                or row - column in occupied_diagonals_down
                or row + column in occupied_diagonals_up
            ):
                continue

            occupied_columns.add(column)
            occupied_diagonals_down.add(row - column)
            occupied_diagonals_up.add(row + column)
            placement.append(column)

            backtrack(row + 1)

            placement.pop()
            occupied_columns.remove(column)
            occupied_diagonals_down.remove(row - column)
            occupied_diagonals_up.remove(row + column)

    backtrack(0)
    return solutions


def format_solution(solution: List[int]) -> str:
    """把一个解渲染成棋盘字符串，``Q`` 表示皇后，``.`` 表示空格。"""
    n = len(solution)
    return "\n".join(
        "".join("Q" if column == queen_column else "." for column in range(n))
        for queen_column in solution
    )


if __name__ == "__main__":
    solutions = solve_n_queens(8)
    print(f"八皇后共有 {len(solutions)} 个解。")
    print("其中一个解：")
    print(format_solution(solutions[0]))
