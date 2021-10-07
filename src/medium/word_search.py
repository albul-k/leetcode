"""
Url: https://leetcode.com/problems/word-search/
Author: Konstantin Albul

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Constraints:
* m == board.length
* n = board[i].length
* 1 <= m, n <= 6
* 1 <= word.length <= 15
* board and word consists of only lowercase and uppercase English letters.
"""

from typing import List


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=too-many-arguments
    def recur(self,
              board: List[List[str]],
              word: str,
              row_max: int,
              col_max: int,
              row: int,
              col: int,
              k: int) -> bool:
        """recur

        Parameters
        ----------
        board : List[List[str]]
            characters board
        word : str
            word
        row_max : int
            number of rows
        col_max : int
            number of columns
        row : int
            current row
        col : int
            current column
        k : int
            index of letter in word

        Returns
        -------
        bool
            result
        """

        if len(word) == k:
            return True

        if row < 0 or row >= row_max or col < 0 or col >= col_max:
            return False

        if board[row][col] != word[k]:
            return False

        letter = board[row][col]
        board[row][col] = None
        for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if self.recur(board, word, row_max, col_max, row + i, col + j, k + 1):
                return True
        board[row][col] = letter
        return False

    # pylint: disable=no-self-use
    def exist(self, board: List[List[str]], word: str) -> bool:
        """word-search

        Parameters
        ----------
        board : List[List[str]]
            characters board
        word : str
            word

        Returns
        -------
        bool
            result
        """

        row_max = len(board)
        col_max = len(board[0])
        for row in range(row_max):
            for col in range(col_max):
                if self.recur(board, word, row_max, col_max, row, col, 0):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") is True
    assert solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") is True
    assert solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") is False
    assert solution.exist([["a","a"]], "aaa") is False
