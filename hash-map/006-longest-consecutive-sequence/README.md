# Longest Consecutive Sequence — LeetCode 128 (Medium)

**Pattern:** Hash Set / Sequence Starts (Stage 1 of the starter guide)

## Problem
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

- In `[100,4,200,1,3,2]`, the numbers `1,2,3,4` form a run of length 4, so the answer is `4`.

## Examples
1. `nums = [100,4,200,1,3,2]` → `4`
2. `nums = [0,3,7,2,5,8,4,6,0,1]` → `9`

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints (read one at a time — try before reading the next)
1. **Brute force first:** sort the array and scan for runs. That works — what is its time complexity, and why does it break the O(n) requirement?
2. **The tool:** a hash set, for O(1) "is this number here?" checks. But if you count forward from every number, how many times do you visit the same run?
3. **The key question:** from which numbers is it worth starting to count? Only the ones that have no predecessor — what does that check look like?

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (An empty array, and an array of all duplicates.)
- How is this the same set idea as Contains Duplicate — and what is new?

## Result (2026-11-25, user Jadu2049)
Accepted: **85/85 test cases; 43 ms, beats 92.00%**; **36.49 MB, beats 78.27%**.
Solved with the sequence-start approach: put everything in a set, only count forward from numbers whose predecessor is missing, track the longest run.
