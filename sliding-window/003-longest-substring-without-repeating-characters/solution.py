"""Longest Substring Without Repeating Characters — LeetCode 3 (Medium).

Sliding window: a window that only ever holds distinct characters.
Expand the right end; when a duplicate appears, shrink from the left
until it is gone. Track the longest window seen.

Run the tests:  python solution.py
"""


def length_of_longest_substring(s):
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        # Shrink from the left until the duplicate is out of the window.
        # A while (not if): sometimes more than one char must go.
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def lengthOfLongestSubstring(self, s):
        return length_of_longest_substring(s)


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abcdef") == 6
    print("All 5 tests passed.")
