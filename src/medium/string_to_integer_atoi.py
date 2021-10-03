"""
Url: https://leetcode.com/problems/string-to-integer-atoi/
Author: Konstantin Albul

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'.
Read this character in if it is either.
This determines if the final result is negative or positive respectively.
Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached.
The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
then clamp the integer so that it remains in the range.

Specifically, integers less than -2*31 should be clamped to -2*31,
and integers greater than 2*31 - 1 should be clamped to 2*31 - 1.

Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or
the rest of the string after the digits.

Constraints:
* 0 <= s.length <= 200
* s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    def __init__(self) -> None:
        """Init
        """
        self.min_val: int = -2 ** 31
        self.max_val: int = (2 ** 31) - 1

    # pylint: disable=no-self-use
    # pylint: disable=invalid-name
    def my_atoi(self, s: str) -> int:
        """string-to-integer-atoi

        Parameters
        ----------
        s : str
            string

        Returns
        -------
        int
            integer
        """

        numbers: list = []
        output: int = 0
        for char in s:
            if len(numbers) == 0 and char == ' ':
                continue
            if len(numbers) == 0 and char in ('+', '-'):
                numbers.append(char)
                continue
            if not char.isdigit():
                if len(numbers) > 0 and numbers[-1] in ('+', '-'):
                    numbers = []
                break
            numbers.append(char)

        if len(numbers) == 0:
            return output
        try:
            output = int(''.join(numbers))
            if output < self.min_val:
                return self.min_val
            if output > self.max_val:
                return self.max_val
            return output
        except ValueError:
            return output


if __name__ == "__main__":
    solution = Solution()

    assert solution.my_atoi("42") == 42
    assert solution.my_atoi("   -42") == -42
    assert solution.my_atoi("4193 with words") == 4193
    assert solution.my_atoi("words and 987") == 0
    assert solution.my_atoi("-91283472332") == -2 ** 31
    assert solution.my_atoi("91283472332") == (2 ** 31) - 1
    assert solution.my_atoi("3.14159") == 3
    assert solution.my_atoi(" 3.14159") == 3
    assert solution.my_atoi(" -3.14159") == -3
    assert solution.my_atoi(" - 3.14159") == 0
    assert solution.my_atoi(" -.14159") == 0
    assert solution.my_atoi(" -0.14159") == 0
    assert solution.my_atoi(" -0") == 0
