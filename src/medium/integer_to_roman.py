"""
Url: https://leetcode.com/problems/integer-to-roman/
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
* 1 <= num <= 3999
"""


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def int_to_roman(self, num: int) -> str:
        """integer_to_roman

        Parameters
        ----------
        num : int
            integer number

        Returns
        -------
        str
            roman number
        """

        roman_numbers: tuple = (
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
        )

        output: str = ''
        num_tmp: int = num
        for (roman_num, num_) in roman_numbers:
            if num_ > num_tmp:
                continue

            modulo: int = num_tmp // num_
            if modulo > 0:
                output += roman_num * modulo

            num_tmp = num_tmp % num_

            if num_tmp == 0:
                break

        return output


if __name__ == "__main__":
    solution = Solution()

    assert solution.int_to_roman(3) == "III"
    assert solution.int_to_roman(4) == "IV"
    assert solution.int_to_roman(9) == "IX"
    assert solution.int_to_roman(58) == "LVIII"
    assert solution.int_to_roman(1994) == "MCMXCIV"
