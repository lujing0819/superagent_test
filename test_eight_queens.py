"""eight_queens.py 的测试。运行：python3 -m unittest -v"""

import unittest

from eight_queens import format_solution, solve_n_queens


class EightQueensTests(unittest.TestCase):
    def test_known_solution_counts(self):
        # n 皇后问题已知的解数量，其中八皇后有 92 个解。
        expected_counts = {
            1: 1,
            2: 0,
            3: 0,
            4: 2,
            5: 10,
            6: 4,
            7: 40,
            8: 92,
        }
        for n, expected in expected_counts.items():
            with self.subTest(n=n):
                self.assertEqual(len(solve_n_queens(n)), expected)

    def test_default_solves_eight_queens(self):
        self.assertEqual(len(solve_n_queens()), 92)

    def test_every_solution_is_valid(self):
        for n in (4, 5, 6, 7, 8):
            for solution in solve_n_queens(n):
                with self.subTest(n=n, solution=solution):
                    self.assertEqual(len(solution), n)
                    # 每一行恰好一个皇后，并且列号不重复。
                    self.assertEqual(sorted(solution), list(range(n)))
                    # 两条斜线也不能有冲突。
                    self.assertEqual(
                        len({row - column for row, column in enumerate(solution)}),
                        n,
                    )
                    self.assertEqual(
                        len({row + column for row, column in enumerate(solution)}),
                        n,
                    )

    def test_solutions_are_unique(self):
        solutions = solve_n_queens(8)
        self.assertEqual(len({tuple(solution) for solution in solutions}), 92)

    def test_rejects_non_positive_board_size(self):
        for n in (0, -1):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    solve_n_queens(n)

    def test_format_solution(self):
        self.assertEqual(
            format_solution([1, 3, 0, 2]),
            ".Q..\n"
            "...Q\n"
            "Q...\n"
            "..Q.",
        )


if __name__ == "__main__":
    unittest.main()
