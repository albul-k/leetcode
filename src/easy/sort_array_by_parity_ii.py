"""
Url: https://leetcode.com/explore/item/3990
Author: Konstantin Albul

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Constraints:
* 2 <= nums.length <= 2 * 104
* nums.length is even.
* Half of the integers in nums are even.
* 0 <= nums[i] <= 1000
"""

from typing import List


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def sort_array_by_parity_ii(self, nums: List[int]) -> List[int]:
        """Sort Array By Parity II

        Parameters
        ----------
        nums : List[int]
            array of integers nums

        Returns
        -------
        List[int]
            sorted array
        """

        wrong_even_idx: list = []
        wrong_odd_idx: list = []
        for idx, num in enumerate(nums):
            if idx & 1 == 0 and num & 1 != 0:
                wrong_even_idx.append(idx)
            elif idx & 1 != 0 and num & 1 == 0:
                wrong_odd_idx.append(idx)

        for (idx_even, idx_odd) in zip(wrong_even_idx, wrong_odd_idx):
            nums[idx_even], nums[idx_odd] = nums[idx_odd], nums[idx_even]

        return nums


if __name__ == "__main__":
    solution = Solution()

    assert solution.sort_array_by_parity_ii([4,2,5,7]) == [4,5,2,7]
    assert solution.sort_array_by_parity_ii([3,2]) == [2,3]
    assert solution.sort_array_by_parity_ii([3,2,3,2]) == [2,3,2,3]
    assert solution.sort_array_by_parity_ii([2,3]) == [2,3]
