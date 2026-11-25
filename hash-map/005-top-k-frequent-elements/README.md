# Top K Frequent Elements — LeetCode 347 (Medium)

**Pattern:** Hash Map + Bucket Sort (Stage 1 of the starter guide)

## Problem
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

- In `[1,1,1,2,2,3]` with `k = 2`, `1` appears 3 times and `2` appears twice, so the answer is `[1,2]`.

## Examples
1. `nums = [1,1,1,2,2,3]`, `k = 2` → `[1,2]`
2. `nums = [1]`, `k = 1` → `[1]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`
- It is guaranteed that the answer is unique.

## Follow-up
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Hints (read one at a time — try before reading the next)
1. **First step:** what do you need to know about each number? The same thing as Valid Anagram — *how many times does it appear?*
2. **The trap:** sorting the numbers by frequency works, but that is O(n log n) — and the follow-up rules it out. What if you sort by frequency without sorting?
3. **The tool:** buckets. A number that appears 3 times goes in bucket 3. How many buckets do you need at most, and which end do you read from?

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (Every number appearing once, and `k` equal to the number of unique elements.)
- How is this the same frequency-counting idea as Valid Anagram and Group Anagrams — and what is new?

## Result (2026-11-25, user Jadu2049)
Accepted: **26/26 test cases; 10 ms, beats 28.14%**; **24.71 MB, beats 12.53%**.
Solved with the bucket-sort approach: count frequencies, drop each number into the bucket matching its count, read buckets from the fullest down until `k` numbers are collected.
