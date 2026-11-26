"""Valid Parentheses — LeetCode 20 (Easy).

A stack does the work: push every opening bracket, and on a closing
bracket check it matches the top of the stack. Mismatch or an empty
stack means invalid; a non-empty stack at the end means something was
never closed. O(n) time, O(n) space.

Run the tests:  python solution.py
"""


def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def isValid(self, s):
        return is_valid(s)


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    assert is_valid("(((") is False
    print("All 7 tests passed.")
