# Contains Duplicate — LeetCode 217 (Easy)

**Pattern:** Hash Map / Hash Set Lookup (Stage 1 of the starter guide)

## Problem
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

- Only the values matter — the positions do not.
- In `[1, 2, 3, 1]`, the value `1` appears at indices 0 and 3, so the answer is `true`.

## Examples
1. `nums = [1, 2, 3, 1]` → `true`
2. `nums = [1, 2, 3, 4]` → `false`
3. `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]` → `true`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints (read one at a time — try before reading the next)
1. **Brute force first:** for each number, check every other number. That works — what is its time complexity, and why is it slow when `n` can be 100,000?
2. **The key question:** as you walk through the list once, what do you need to remember? Only one thing: *have I seen this number before?*
3. **The tool:** a hash set — the same idea as Two Sum's dict, but here you only need to remember *whether* you have seen a value, not *where* it was. For each number, check whether it is already in the set before you add it. What should you return the moment you find one that is already there — and what if you finish the whole list without finding one?
4. **A second way to think about it (for after you solve it):** a set keeps only one copy of each value. What does that say about the size of the set compared with the size of the list when there is a duplicate?

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (A list with one element, and a duplicate right at the start vs right at the end.)
- How is this different from Two Sum — and how is it the same idea?

## Result (2026-11-23, user Jadu2049)
Accepted: **17 ms, beats 51.87%**; **32.98 MB, beats 38.69%**.
Solved with the hash-set approach: check each number against the set of seen
values before adding it, return `True` on the first repeat.
