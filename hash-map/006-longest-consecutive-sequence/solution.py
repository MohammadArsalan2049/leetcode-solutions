"""Longest Consecutive Sequence — LeetCode 128 (Medium).

Put everything in a set, then only count forward from numbers whose
predecessor is missing — those are the starts of runs. Each number is
visited at most twice, so the whole thing is O(n) with no sorting.

Run the tests:  python solution.py
"""


def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        # Only a run's start is worth counting from.
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def longestConsecutive(self, nums):
        return longest_consecutive(nums)


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1, 2, 2, 3]) == 3
    assert longest_consecutive([10]) == 1
    print("All 5 tests passed.")
