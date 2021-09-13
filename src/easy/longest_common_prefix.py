"""
Url: https://leetcode.com/problems/longest-common-prefix/
Author: Konstantin Albul

Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:
* 1 <= strs.length <= 200
* 0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

from typing import List


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def longest_common_prefix(self, strs: List[str]) -> str:
        """longest-common-prefix

        Parameters
        ----------
        strs : List[str]
            list of strings

        Returns
        -------
        str
            prefix
        """

        if len(strs) == 1:
            return strs[0]

        output: str = ""
        for itm in zip(*strs):
            if len(set(itm)) == 1:
                output += itm[0]
            else:
                break

        return output


if __name__ == "__main__":
    solution = Solution()

    assert solution.longest_common_prefix(["flower","flow","flight"]) == "fl"
    assert solution.longest_common_prefix(["dog","racecar","car"]) == ""
    assert solution.longest_common_prefix(["dog"]) == "dog"
