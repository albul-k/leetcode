"""
Url: https://leetcode.com/problems/perfect-squares/
Author: Konstantin Albul

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Constraints:
* 1 <= n <= 104
"""

from math import sqrt


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def num_squares(self, num: int) -> int:
        """perfect-squares

        Parameters
        ----------
        num : int
            integer

        Returns
        -------
        int
            The least number of perfect square numbers
        """

        perfect_squares: list = [i * i for i in range(1, int(sqrt(num)) + 1)]
        tmp: list = [float("inf") for i in range(num + 1)]
        tmp[0], tmp[1] = 0, 1
        for i in range(2, num + 1):
            for square in perfect_squares:
                tmp[i] = min(tmp[i], tmp[i - square] + 1)
        return tmp[-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.num_squares(12) == 3
    assert solution.num_squares(13) == 2
    assert solution.num_squares(2) == 2
    assert solution.num_squares(1) == 1
    assert solution.num_squares(3) == 3
    assert solution.num_squares(4) == 1
