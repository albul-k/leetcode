"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        str_x: str = str(x)
        if x < 0:
            str_x = '-'+str_x[::-1][:-1]
        else:
            str_x = str_x[::-1]

        x: int = int(str_x)

        if abs(x) < 2**31 and x != 2**31 - 1:
           return x
        else:
           return 0


if __name__ == "__main__":
    solution = Solution()

    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(0) == 0
