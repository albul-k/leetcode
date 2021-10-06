"""
Url: https://leetcode.com/problems/find-all-duplicates-in-an-array/
Author: Konstantin Albul

Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Constraints:
* n == nums.length
* 1 <= n <= 105
* 1 <= nums[i] <= n
* Each element in nums appears once or twice.
"""

from typing import List


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def find_duplicates(self, nums: List[int]) -> List[int]:
        """find-all-duplicates-in-an-array

        Parameters
        ----------
        nums : List[int]
            array nums

        Returns
        -------
        List[int]
            array of dublicates
        """

        uniques: set = set()
        dublicates: list = []

        while nums:
            num = nums.pop()
            if num not in uniques:
                uniques.add(num)
            else:
                dublicates.append(num)

        return dublicates


if __name__ == "__main__":
    solution = Solution()

    assert solution.find_duplicates([4,3,2,7,8,2,3,1]) == [2,3]
    assert solution.find_duplicates([1,1,2]) == [1]
    assert solution.find_duplicates([1]) == []
