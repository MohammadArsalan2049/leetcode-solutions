"""Two Sum — LeetCode 1 (Easy).

Solved 2026-11-14, first LeetCode problem. Accepted on LeetCode:
66/66 test cases, 0 ms (beats 100%), 20.32 MB.

Idea: for each number x, the partner you need is target - x.
A dict remembers every number seen so far and its index, so the
partner lookup is O(1). Check before you store, so you never reuse
the same element twice.

Run the tests:  python solution.py
"""


def two_sum(nums, target):
    seen = {}  # number -> its index
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
    return []


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def twoSum(self, nums, target):
        return two_sum(nums, target)


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) in ([0, 1], [1, 0])
    assert two_sum([3, 2, 4], 6) in ([1, 2], [2, 1])
    assert two_sum([3, 3], 6) in ([0, 1], [1, 0])
    print("All 3 tests passed.")
