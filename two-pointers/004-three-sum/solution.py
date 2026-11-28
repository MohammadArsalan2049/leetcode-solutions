"""3Sum — LeetCode 15 (Medium).

Sort first, then fix one number and use two pointers on the rest to
find pairs summing to its negative. Duplicates are skipped at all
three positions: the fixed index, and both pointers after a hit.
O(n^2) time, O(1) extra space besides the output.

Run the tests:  python solution.py
"""


def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def threeSum(self, nums):
        return three_sum(nums)


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    assert three_sum([1, 2, -2, -1]) == []
    print("All 5 tests passed.")
