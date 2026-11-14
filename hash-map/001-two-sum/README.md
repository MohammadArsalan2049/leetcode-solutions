# Two Sum — LeetCode 1 (Easy)

**Pattern:** Hash Map Lookup (Stage 1 of the starter guide)

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

- There is exactly one solution.
- You may not use the same element twice.
- You may return the answer in any order.

## Examples
1. `nums = [2, 7, 11, 15]`, `target = 9` → `[0, 1]` (because 2 + 7 = 9)
2. `nums = [3, 2, 4]`, `target = 6` → `[1, 2]`
3. `nums = [3, 3]`, `target = 6` → `[0, 1]`

## Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists.

## Hints (read one at a time — try before reading the next)
1. **Brute force first:** for each number, check every other number. That works — what is its time complexity, and why is it slow?
2. **The key question:** for a number `x`, what other number do you need? (`target - x`.) If you could look that up instantly, the whole problem becomes one pass.
3. **The tool:** a hash map from *value → index*, built as you go. For each `x`, check whether `target - x` is already in the map before you add `x` itself. Why does the order — check first, then add — matter?

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (Same element twice, duplicate values like `[3, 3]`.)
