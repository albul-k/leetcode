"""
Url: https://leetcode.com/problems/two-sum/
Author: Konstantin Albul

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Constraints:
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.
"""

from typing import List

# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """two-sum

        Parameters
        ----------
        nums : List[int]
            array of integers nums
        target : int
            integer target

        Returns
        -------
        List[int]
            indices of the two numbers
        """

        output: list = []

        for i in range(0, len(nums) - 1, 1):
            for k in range(i + 1, len(nums), 1):
                if nums[i] + nums[k] == target:
                    output.append(i)
                    output.append(k)
                    break
            if output:
                break

        return output


if __name__ == "__main__":
    solution = Solution()

    assert solution.two_sum([2,7,11,15], 9) == [0,1]
    assert solution.two_sum([3,2,4], 6) == [1,2]
    assert solution.two_sum([3,3], 6) == [0,1]
