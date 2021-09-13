"""
Url: https://leetcode.com/problems/reverse-integer/
Author: Konstantin Albul

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside
the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:
* -231 <= x <= 231 - 1
"""


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def reverse(self, x_int: int) -> int:
        """reverse-integer

        Parameters
        ----------
        x_int : int
            integer

        Returns
        -------
        int
            reverse integer
        """

        str_x: str = str(x_int)
        if x_int < 0:
            str_x = '-' + str_x[::-1][:-1]
        else:
            str_x = str_x[::-1]

        output: int = int(str_x)

        if abs(output) < 2**31 and output != 2**31 - 1:
            return output
        return 0


if __name__ == "__main__":
    solution = Solution()

    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(0) == 0
