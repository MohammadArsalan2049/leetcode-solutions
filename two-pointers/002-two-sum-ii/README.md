# Two Sum II — Input Array Is Sorted — LeetCode 167 (Easy)

**Pattern:** Two Pointers (Stage 2 of the starter guide)

## Problem
Given a **1-indexed** array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers, `index1` and `index2`, as an integer array `[index1, index2]` of length 2. There is exactly one solution, and you may not use the same element twice. Your solution must use only constant extra space.

## Examples
1. `numbers = [2, 7, 11, 15], target = 9` → `[1, 2]` (2 + 7 = 9)
2. `numbers = [2, 3, 4], target = 6` → `[1, 3]` (2 + 4 = 6)
3. `numbers = [-1, 0], target = -1` → `[1, 2]` (-1 + 0 = -1)

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.

## Hints (read one at a time — try before reading the next)
1. **The sorted clue:** the array is sorted — that is the whole point of this problem. What does sorted order let you decide from the sum of two numbers?
2. **The tool:** two pointers, one at each end. If the sum is too small, which end must move, and why?
3. **The gotcha:** the answer is 1-indexed. The pointers are 0-indexed, so add 1 to each before returning.

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (The pair sits at the very ends, or the two numbers are next to each other.)

## Result (2026-11-28, user Jadu2049)
Accepted: **26/26 test cases; 7 ms, beats 57.31%**; **22.51 MB, beats 18.60%**.
Solved with two pointers from both ends of the sorted array, moving the left pointer right when the sum is too small and the right pointer left when it is too big, returning 1-indexed positions.
