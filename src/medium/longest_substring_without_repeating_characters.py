"""
Url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Author: Konstantin Albul

Given a string s, find the length of the longest substring without repeating characters.

Constraints:
* 0 <= s.length <= 5 * 104
* s consists of English letters, digits, symbols and spaces.
"""


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def length_of_longest_substring(self, s_str: str) -> int:
        """longest-substring-without-repeating-characters

        Parameters
        ----------
        s_str : str
            substring

        Returns
        -------
        int
            lenthg of longest substring
        """

        if s_str == "":
            return 0
        if len(set(s_str)) == 1:
            return 1

        substr: str = ''
        substr_length: int = 0
        counter: int = 0
        end: bool = False
        chars: set = set()
        for start in range(0, len(s_str)):
            for char in s_str[start::]:
                if char not in chars:
                    chars.add(char)
                    substr += char
                    counter += 1
                else:
                    if s_str[start::].replace(substr, '') == '':
                        end = True
                        break

                    chars.clear()
                    chars.add(char)
                    counter = 1

                if counter > substr_length:
                    substr_length = counter

            if end:
                break

            chars.clear()
            substr = ''
            counter = 0

        return substr_length


if __name__ == "__main__":
    solution = Solution()

    assert solution.length_of_longest_substring("abcabcbb") == 3
    assert solution.length_of_longest_substring("bbbbb") == 1
    assert solution.length_of_longest_substring("pwwkew") == 3
    assert solution.length_of_longest_substring("") == 0
    assert solution.length_of_longest_substring("dvdf") == 3
    assert solution.length_of_longest_substring("asjrgapa") == 6

    TEST_STR = "abcdefghijklmnopqrstuvwxyz"
    TEST_STR += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    TEST_STR += "0123456789"
    TEST_STR += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    assert solution.length_of_longest_substring(TEST_STR * 10) == 95
