# Longest Palindromic Substring — LeetCode 5 (Medium)

**Pattern:** Expand Around Center (two pointers)

## Problem
Given a string `s`, return the longest palindromic substring in `s`.

## Examples
1. `s = "babad"` → `"bab"` ("aba" is also a valid answer)
2. `s = "cbbd"` → `"bb"`

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

## Approach
A palindrome mirrors around its middle, so every index is a possible center —
two kinds per index:

- **Odd length:** the center is a character — `expand(i, i)` ("bab" centers on `a`).
- **Even length:** the center is between two characters — `expand(i, i + 1)`
  ("bb" centers between the two `b`s).

`expand(left, right)` steps both pointers outward while the characters match.
When they stop, both pointers are one step past the palindrome, so it returns
`left + 1, right - 1`. The main loop keeps the longest palindrome found; the
`>` (not `>=`) comparison means the first palindrome wins on a tie, which is
why `"babad"` returns `"bab"` and not `"aba"`.

## Complexity
- Time: O(n^2) — 2n-1 centers, each expanding up to O(n) steps.
- Space: O(1) — no table, unlike the DP version.

## Result (2026-11-23, user Jadu2049)
Accepted: **248 ms, beats 72.04%**; **18.94 MB, beats 96.88%**.
