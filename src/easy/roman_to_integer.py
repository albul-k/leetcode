"""
Url: https://leetcode.com/problems/roman-to-integer/
Author: Konstantin Albul

Roman numerals are represented by seven different symbols:
* I
* V
* X
* L
* C
* D
* M

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral,
just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
* I can be placed before V (5) and X (10) to make 4 and 9.
* X can be placed before L (50) and C (100) to make 40 and 90.
* C can be placed before D (500) and M (1000) to make 400 and 900.
* Given a roman numeral, convert it to an integer.

Constraints:
* 1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def roman_to_int(self, s_str: str) -> int:
        """roman-to-integer

        Parameters
        ----------
        s_str : str
            roman number

        Returns
        -------
        int
            integer number
        """

        roman_numbers: dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }

        output: int = 0
        skip_next: bool = False
        for idx, _ in enumerate(s_str):
            if skip_next:
                skip_next = False
                continue

            num: int = s_str[idx]
            try:
                num_: int = s_str[idx:idx + 2]
                if num_ in roman_numbers:
                    skip_next = True
                    num = num_
            except KeyError:
                pass
            output += roman_numbers[num]
        return output


if __name__ == "__main__":
    solution = Solution()

    assert solution.roman_to_int("III") == 3
    assert solution.roman_to_int("IV") == 4
    assert solution.roman_to_int("IX") == 9
    assert solution.roman_to_int("LVIII") == 58
    assert solution.roman_to_int("MCMXCIV") == 1994
