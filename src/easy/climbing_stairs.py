"""
Url: https://leetcode.com/problems/climbing-stairs/
Author: Konstantin Albul

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
* 1 <= n <= 45
"""

from functools import lru_cache


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    @lru_cache(maxsize=None)
    def climb_stairs(self, n_stairs: int) -> int:
        """climbing-stairs

        Parameters
        ----------
        n_stairs : int
            number of stairs

        Returns
        -------
        int
            number of combinations
        """

        if n_stairs < 3:
            return n_stairs
        return self.climb_stairs(n_stairs-1) + self.climb_stairs(n_stairs-2)


if __name__ == "__main__":
    solution = Solution()

    assert solution.climb_stairs(2) == 2
    assert solution.climb_stairs(3) == 3
    assert solution.climb_stairs(4) == 5
