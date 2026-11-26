"""Valid Palindrome — LeetCode 125 (Easy).

Two pointers walk in from both ends, skipping anything that is not
a letter or digit and comparing the rest in lowercase. Any mismatch
means it is not a palindrome; if the pointers meet, it is. O(n) time,
O(1) extra space — no cleaned-up copy of the string is built.

Run the tests:  python solution.py
"""


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def isPalindrome(self, s):
        return is_palindrome(s)


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("ab") is False
    assert is_palindrome("a.") is True
    print("All 5 tests passed.")
