# 3Sum — LeetCode 15 (Medium)

**Pattern:** Two Pointers (Stage 2 of the starter guide)

## Problem
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

## Examples
1. `nums = [-1, 0, 1, 2, -1, -4]` → `[[-1, -1, 2], [-1, 0, 1]]`
2. `nums = [0, 1, 1]` → `[]`
3. `nums = [0, 0, 0]` → `[[0, 0, 0]]`

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Hints (read one at a time — try before reading the next)
1. **The sort first:** sorting the array costs O(n log n) and makes everything else possible. What does sorted order give you?
2. **Reduce it:** fix one number, then the rest is a Two Sum problem — find two numbers that add up to the negative of the fixed one. Which tool solves that?
3. **The duplicates:** the same triplet can be found many ways. Skip the same value for the fixed index, and after each hit, skip past repeated values on both pointers.

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (All zeros — exactly one triplet `[0, 0, 0]`.)

## Result (2026-11-28, user Jadu2049)
Accepted: **316/316 test cases; 650 ms, beats 48.59%**; **22.08 MB, beats 87.63%**.
Solved by sorting, fixing one number at a time, and using two pointers on the rest with duplicate skipping at all three positions.
