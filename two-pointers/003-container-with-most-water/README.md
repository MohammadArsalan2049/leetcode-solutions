# Container With Most Water — LeetCode 11 (Medium)

**Pattern:** Two Pointers (Stage 2 of the starter guide)

## Problem
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`. Find two lines that, together with the x-axis, form a container that holds the most water. Return the maximum amount of water a container can store. You may not slant the container.

## Examples
1. `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]` → `49` (lines at index 1 and 8: height 8 and 7, distance 7 → 7 × 7 = 49)
2. `height = [1, 1]` → `1`

## Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Hints (read one at a time — try before reading the next)
1. **The brute force trap:** checking every pair of lines works, but it is O(n²). The array is long — what lets you skip pairs without checking them?
2. **The tool:** two pointers, one at each end. The area is the shorter line's height times the distance between them.
3. **The move:** always move the pointer at the shorter line inward. The shorter line is what limits the area, so moving the taller one can only shrink the width without raising the limit.

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (All heights equal, or the tallest lines sitting at the two ends.)

## Result (2026-11-28, user Jadu2049)
Accepted: **65/65 test cases; 58 ms, beats 58.61%**; **29.53 MB, beats 66.76%**.
Solved with two pointers from both ends, always moving the pointer at the shorter line inward and tracking the largest area seen.
