"""Container With Most Water — LeetCode 11 (Medium).

Two pointers start at both ends. The area is the shorter line's height
times the distance between the pointers. The shorter line limits the
area, so it is the one that moves inward — moving the taller line can
only shrink the width without raising the limiting height. O(n) time,
O(1) extra space.

Run the tests:  python solution.py
"""


def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = height[left] if height[left] < height[right] else height[right]
        best = max(best, h * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def maxArea(self, height):
        return max_area(height)


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17
    print("All 5 tests passed.")
