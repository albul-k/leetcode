"""
Url: https://leetcode.com/explore/item/3992
Author: Konstantin Albul

Given the head of a singly linked list and an integer k,
split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible:
no two parts should have a size differing by more than one.

This may lead to some parts being null.

The parts should be in the order of occurrence in the input list,
and parts occurring earlier should always have a size greater than
or equal to parts occurring later.

Return an array of the k parts.

Constraints:
* The number of nodes in the list is in the range [0, 1000].
* 0 <= Node.val <= 1000
* 1 <= k <= 50
"""


from typing import Optional, List


# Definition for singly-linked list.
# pylint: disable=too-few-public-methods
class ListNode:
    """ListNode
    """
    # pylint: disable=redefined-builtin
    def __init__(self, val: int = 0, next = None):
        """Init

        Parameters
        ----------
        val : int, optional
            value, by default 0
        next : [type], optional
            ListNode, by default None
        """

        self.val = val
        self.next = next


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """

    # pylint: disable=no-self-use
    def split_list_to_parts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """Split Linked List in Parts

        Parameters
        ----------
        head : Optional[ListNode]
            singly linked list
        k : int
            number of parts

        Returns
        -------
        List[Optional[ListNode]]
            array of the k parts
        """

        curr_node = head
        val_list = []
        while curr_node:
            val_list.append(curr_node.val)
            curr_node = curr_node.next

        output = []

        if len(val_list) / k <= 1:
            for i in range(0, k):
                try:
                    _ = ListNode(val_list[i])
                except IndexError:
                    _ = None
                output.append(_)
        else:
            base, mod = divmod(len(val_list), k)

            for i in range(0, mod):
                curr_node = head
                output.append(head)

                for _ in range(0, base):
                    curr_node = curr_node.next

                head = curr_node.next
                curr_node.next = None

            for i in range(mod, k):
                curr_node = head
                output.append(head)

                for _ in range(0, base - 1):
                    curr_node = curr_node.next

                head = curr_node.next
                curr_node.next = None

        return output


if __name__ == "__main__":
    solution = Solution()

    solution.split_list_to_parts(
        ListNode(1,
            ListNode(2,
                ListNode(3)
            )
        ), 5)
    # [ListNode(1), ListNode(2), ListNode(3), [], []]

    solution.split_list_to_parts(
        ListNode(1,
            ListNode(2,
                ListNode(3,
                    ListNode(4)
                )
            )
        ), 2)
    # [[ListNode(1, ListNode(2))], [ListNode(3, ListNode(4)]]

    solution.split_list_to_parts(
        ListNode(1,
            ListNode(2,
                ListNode(3,
                    ListNode(4,
                        ListNode(5)
                    )
                )
            )
        ), 3)
    # [[ListNode(1, ListNode(2))], [ListNode(3, ListNode(4)], ListNode(5)]

    solution.split_list_to_parts(
        ListNode(1,
            ListNode(2,
                ListNode(3,
                    ListNode(4,
                        ListNode(5,
                            ListNode(6,
                                ListNode(7,
                                    ListNode(8,
                                        ListNode(9,
                                            ListNode(10)
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        ), 3)
    # [
    #     ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
    #     ListNode(5, ListNode(6, ListNode(7))),
    #     ListNode(8, ListNode(9, ListNode(10))),
    # ]
