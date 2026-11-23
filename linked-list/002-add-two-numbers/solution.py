"""Add Two Numbers — LeetCode 2 (Medium).

Digits are stored in reverse order, so the head is the ones place:
add column by column, exactly like school addition, carrying over.

Run the tests:  python solution.py
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(digits):
    dummy = ListNode(0)
    curr = dummy
    for d in digits:
        curr.next = ListNode(d)
        curr = curr.next
    return dummy.next


def linked_list_to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    # Keep going while either list has digits, or a carry is left over.
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def addTwoNumbers(self, l1, l2):
        return add_two_numbers(l1, l2)


if __name__ == "__main__":
    assert linked_list_to_list(add_two_numbers(
        list_to_linked_list([2, 4, 3]), list_to_linked_list([5, 6, 4]))) == [7, 0, 8]
    assert linked_list_to_list(add_two_numbers(
        list_to_linked_list([0]), list_to_linked_list([0]))) == [0]
    assert linked_list_to_list(add_two_numbers(
        list_to_linked_list([9, 9, 9, 9, 9, 9, 9]),
        list_to_linked_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("All 3 tests passed.")
