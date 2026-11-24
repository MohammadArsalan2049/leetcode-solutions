# Valid Anagram — notes

Solved 2026-11-24 (LeetCode 242, Easy). Accepted 56/56, 14 ms, 19.35 MB.

## Approach (in your own words)
Two strings are anagrams when they have the same letters with the same
counts. Count the letters of `s` in a dict, then walk through `t` and
spend one count per letter. If a letter is missing or its count is
already zero, return `False` on the spot. If the loop finishes, every
letter matched, so return `True`.

## Complexity
- Time: O(n) — one pass over each string; each dict lookup and update is O(1) on average.
- Space: O(1) — the dict holds at most 26 lowercase letters, no matter how long the strings are.

## What tripped me up / what I learned
- The first paste failed with `NameError: name 'Solution' is not defined` — the method was pasted without its `class Solution:` wrapper, and LeetCode's driver calls `Solution().isAnagram(...)`. The method has to live inside the class.
- The length check at the top is a quick reject: different lengths can never be anagrams, so there is no point counting.
- One-liner version: `Counter(s) == Counter(t)` — same idea, but building two counters first; the loop version exits early on the first mismatch.

## How it connects to Two Sum and Contains Duplicate
Same hash-lookup family, different job: Two Sum's dict remembers *where* each value was (index) so it can return the pair; Contains Duplicate's set remembers only *whether* a value was seen; here the dict remembers *how many times* each letter appears, because the question is about counts.
