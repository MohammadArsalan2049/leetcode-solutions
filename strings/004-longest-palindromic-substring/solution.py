"""Longest Palindromic Substring — LeetCode 5 (Medium).

Expand around center: a palindrome mirrors around its middle, so every
index is a possible center — odd length (center is a character) and even
length (center is between two characters). Expand outward from each center
and keep the longest palindrome found.

Run the tests:  python solution.py
"""


def longest_palindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Both pointers are now one step past the palindrome.
        return left + 1, right - 1

    start, end = 0, 0
    for i in range(len(s)):
        l1, r1 = expand(i, i)      # odd length, center is s[i]
        l2, r2 = expand(i, i + 1)  # even length, center is between i and i+1
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end + 1]


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def longestPalindrome(self, s):
        return longest_palindrome(s)


if __name__ == "__main__":
    assert longest_palindrome("babad") == "bab"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    print("All 5 tests passed.")
