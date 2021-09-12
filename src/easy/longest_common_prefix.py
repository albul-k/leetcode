"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

from typing import List


class Solution:
    """
    longestCommonPrefix
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """longestCommonPrefix

        Parameters
        ----------
        strs : List[str]
            [description]

        Returns
        -------
        str
            [description]
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

    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert solution.longestCommonPrefix(["dog"]) == "dog"
