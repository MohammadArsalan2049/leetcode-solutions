"""Contains Duplicate — LeetCode 217 (Easy).

One pass, one question per number: have I seen you before? A hash set
remembers only *whether* a value was seen — no index tracking like Two Sum.

Run the tests:  python solution.py
"""


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        # Check BEFORE adding — that is what makes it a duplicate check.
        if num in seen:
            return True
        seen.add(num)
    return False


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def containsDuplicate(self, nums):
        return contains_duplicate(nums)


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate([1]) is False
    print("All 4 tests passed.")
