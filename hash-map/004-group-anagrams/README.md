# Group Anagrams — LeetCode 49 (Medium)

**Pattern:** Hash Map / Grouping by Key (Stage 1 of the starter guide)

## Problem
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word formed by rearranging the letters of another — same letters, same counts, different order.

- `"eat"`, `"tea"` and `"ate"` are anagrams of each other, so they belong in one group.
- `"tan"` and `"nat"` form a second group; `"bat"` is on its own.

## Examples
1. `strs = ["eat","tea","tan","ate","nat","bat"]` → `[["bat"],["nat","tan"],["ate","eat","tea"]]`
2. `strs = [""]` → `[[""]]`
3. `strs = ["a"]` → `[["a"]]`

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Hints (read one at a time — try before reading the next)
1. **The key question:** what single value is the same for two anagrams and different for two non-anagrams? Think back to Valid Anagram — what did you compare there?
2. **The tool:** a hash map from that key to a list of words. Walk the list once; for each word, compute its key and append the word to that key's list.
3. **A second way to build the key (for after you solve it):** instead of sorting the letters, count them — a 26-length tuple of counts works as a key too, and avoids the sort. Which is faster, and when does it matter?

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (An empty string, and a list with one word.)
- How is this the same idea as Valid Anagram — and what is different?

## Result (2026-11-25, user Jadu2049)
Accepted: **130/130 test cases; 12 ms, beats 68.64%**; **21.72 MB, beats 90.72%**.
Solved with the sorted-key approach: sort each word's letters to make the key, group words by that key in a dict of lists.
