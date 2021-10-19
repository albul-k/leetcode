"""
Url: https://leetcode.com/problems/next-greater-element-i/
Author: Konstantin Albul

The next greater element of some element x in an array
is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2,
where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i]
is the next greater element as described above.

Constraints:
* 1 <= nums1.length <= nums2.length <= 1000
* 0 <= nums1[i], nums2[i] <= 104
* All integers in nums1 and nums2 are unique.
* All the integers of nums1 also appear in nums2.
"""

from typing import List


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """next-greater-element-i

        Parameters
        ----------
        nums1 : List[int]
            first array
        nums2 : List[int]
            second array

        Returns
        -------
        List[int]
            array
        """

        nums2_dict = {value: idx for idx, value in enumerate(nums2)}
        output = [-1 for _ in range(len(nums1))]
        for idx, num in enumerate(nums1):
            for idx_2 in range(nums2_dict[num]+1, len(nums2)):
                if nums2[idx_2] > num:
                    output[idx] = nums2[idx_2]
                    break
        return output


if __name__ == "__main__":
    solution = Solution()

    assert solution.next_greater_element(nums1 = [4,1,2], nums2 = [1,3,4,2]) == [-1,3,-1]
    assert solution.next_greater_element(nums1 = [2,4], nums2 = [1,2,3,4]) == [3,-1]
