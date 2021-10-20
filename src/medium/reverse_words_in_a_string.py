"""
Url: https://leetcode.com/problems/reverse-words-in-a-string/
Author: Konstantin Albul

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Constraints:
* 1 <= s.length <= 104
* s contains English letters (upper-case and lower-case), digits, and spaces ' '.
* There is at least one word in s.
"""


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def reverse_words(self, s_str: str) -> str:
        """reverse-words-in-a-string

        Parameters
        ----------
        s_str : str
            given string

        Returns
        -------
        str
            reversed string
        """

        output = []
        for word in s_str.split()[::-1]:
            if word == '':
                continue
            output.append(word)

        return ' '.join(output)


if __name__ == "__main__":
    solution = Solution()

    assert solution.reverse_words(s_str = "the sky is blue") == "blue is sky the"
    assert solution.reverse_words(s_str = "  hello world  ") == "world hello"
    assert solution.reverse_words(s_str = "a good   example") == "example good a"
    assert solution.reverse_words(s_str = "  Bob    Loves  Alice   ") == "Alice Loves Bob"
    assert solution.reverse_words(
        s_str = "Alice does not even like bob") == "bob like even not does Alice"
