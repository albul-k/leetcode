"""
Url: https://leetcode.com/problems/add-two-numbers/
Author: Konstantin Albul

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
* The number of nodes in each linked list is in the range [1, 100].
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional


# pylint: disable=too-few-public-methods
class ListNode:
    """ListNode
    """

    # pylint: disable=no-self-use
    # pylint: disable=redefined-builtin
    def __init__(self, val=0, next=None):
        """ListNode Init

        Parameters
        ----------
        val : int, optional
            integer, by default 0
        next : ListNode, optional
            ListNode, by default None
        """
        self.val = val
        self.next = next


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def add_two_numbers(
        self,
        l_1: Optional[ListNode],
        l_2: Optional[ListNode]) -> Optional[ListNode]:
        """add_two_numbers

        Parameters
        ----------
        l_1 : Optional[ListNode]
            linked list #1
        l_2 : Optional[ListNode]
            linked list #2

        Returns
        -------
        Optional[ListNode]
            Sum as a linked list
        """

        list_node = ListNode()
        curr_node = list_node
        carry=0
        while l_1 or l_2 or carry:
            sum_ = 0
            if l_1:
                sum_ += l_1.val
                l_1 = l_1.next
            if l_2:
                sum_ += l_2.val
                l_2 = l_2.next
            if carry:
                sum_ += carry

            val=sum_ % 10
            carry=sum_ // 10

            curr_node.next = ListNode(val)
            curr_node = curr_node.next

        return list_node.next
