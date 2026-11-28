"""Two Sum II — Input Array Is Sorted — LeetCode 167 (Easy).

The array is already sorted, so two pointers are enough — no hash map
needed. Add the numbers at both ends: if the sum is smaller than the
target, the left pointer must move right; if it is bigger, the right
pointer must move left. When the sum matches, return the two positions
1-indexed. O(n) time, O(1) extra space.

Run the tests:  python solution.py
"""


def two_sum_ii(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def twoSum(self, numbers, target):
        return two_sum_ii(numbers, target)


if __name__ == "__main__":
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_ii([2, 3, 4], 6) == [1, 3]
    assert two_sum_ii([-1, 0], -1) == [1, 2]
    assert two_sum_ii([1, 2, 3, 4, 5], 9) == [4, 5]
    assert two_sum_ii([5, 25, 75], 100) == [2, 3]
    print("All 5 tests passed.")
