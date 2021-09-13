"""
Url: https://leetcode.com/problems/palindrome-number/
Author: Konstantin Albul

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Constraints:
* -231 <= x <= 231 - 1
"""

# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def is_palindrome(self, x_int: int) -> bool:
        """palindrome-number

        Parameters
        ----------
        x_int : int
            integer

        Returns
        -------
        bool
            is integer a palindrome
        """

        x_str: str = str(x_int)
        return x_str == ''.join(reversed(x_str))


if __name__ == "__main__":
    solution = Solution()

    assert solution.is_palindrome(121) is True
    assert solution.is_palindrome(-121) is False
    assert solution.is_palindrome(10) is False
    assert solution.is_palindrome(-101) is False
