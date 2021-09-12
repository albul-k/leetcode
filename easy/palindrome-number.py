"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str: str = str(x)
        return x_str == ''.join(reversed(x_str))


if __name__ == "__main__":
    solution = Solution()

    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False
    assert solution.isPalindrome(-101) == False
