"""
Url: https://leetcode.com/problems/min-stack/
Author: Konstantin Albul

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
* MinStack() initializes the stack object.
* void push(int val) pushes the element val onto the stack.
* void pop() removes the element on the top of the stack.
* int top() gets the top element of the stack.
* int getMin() retrieves the minimum element in the stack.

Constraints:
* -2^31 <= val <= 2^31 - 1
* Methods pop, top and getMin operations will always be called on non-empty stacks.
* At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


# pylint: disable=too-few-public-methods
class MinStack:
    """solution
    """

    # pylint: disable=no-self-use
    def __init__(self):
        """init
        """

        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        """push

        Parameters
        ----------
        val : int
            value
        """

        self.stack.append(val)
        if not self.min_val:
            val_ = val
        else:
            val_ = min(val, self.getMin())
        self.min_val.append(val_)

    def pop(self) -> None:
        """pop
        """

        self.stack.pop()
        self.min_val.pop()

    def top(self) -> int:
        """Get top element of stack

        Returns
        -------
        int
            value
        """

        return self.stack[-1]

    def get_min(self) -> int:
        """Get the minimum element of stack

        Returns
        -------
        int
            value
        """

        return self.min_val[-1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(4)
    obj.push(5)
    assert obj.top() == 5
    obj.pop()
    assert obj.get_min() == 4
