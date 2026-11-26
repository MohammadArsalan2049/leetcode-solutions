# Valid Palindrome — LeetCode 125 (Easy)

**Pattern:** Two Pointers (Stage 2 of the starter guide)

## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples
1. `s = "A man, a plan, a canal: Panama"` → `true`
2. `s = "race a car"` → `false`
3. `s = " "` → `true`

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Hints (read one at a time — try before reading the next)
1. **The cleaning trap:** building a cleaned copy of the string first works, but it costs O(n) extra space. Can you check the string as it is?
2. **The tool:** two pointers, one at each end, skipping characters that are not alphanumeric.
3. **The comparison:** compare in lowercase, and move both pointers inward after each match.

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (A string of only spaces or punctuation — it is a palindrome.)

## Result (2026-11-26, user Jadu2049)
Accepted: **492/492 test cases; 9 ms, beats 47.82%**; **19.40 MB, beats 88.10%**.
Solved with two pointers: skip non-alphanumerics, compare lowercased characters from both ends, and require the pointers to meet.
