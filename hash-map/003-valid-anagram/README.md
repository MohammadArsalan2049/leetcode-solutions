# Valid Anagram — LeetCode 242 (Easy)

**Pattern:** Hash Map / Frequency Counting (Stage 1 of the starter guide)

## Problem
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of another — same letters, same counts, different order.

- In `"anagram"` and `"nagaram"`, every letter appears the same number of times, so the answer is `true`.
- In `"rat"` and `"car"`, the letters differ, so the answer is `false`.

## Examples
1. `s = "anagram"`, `t = "nagaram"` → `true`
2. `s = "rat"`, `t = "car"` → `false`

## Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Hints (read one at a time — try before reading the next)
1. **Brute force first:** sort both strings and compare them. That works — what is its time complexity, and can you do better than sorting?
2. **The key question:** what do you actually need to know about each string? Only one thing: *how many times does each letter appear?*
3. **The tool:** a hash map that counts letters. Count the letters of `s`, then walk through `t` and spend one count per letter. What should happen the moment a letter is missing or its count hits zero?
4. **A quick reject (for before you count anything):** if the two strings have different lengths, can they ever be anagrams?

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (Same word twice, and strings that differ by one letter.)
- How is this different from Two Sum and Contains Duplicate — and how is it the same idea?

## Result (2026-11-24, user Jadu2049)
Accepted: **56/56 test cases; 14 ms, beats 42.14%**; **19.35 MB, beats 72.00%**.
Solved with the frequency-count approach: count the letters of `s` in a dict, then spend one count per letter of `t`, returning `False` the moment a letter is missing or used up.
