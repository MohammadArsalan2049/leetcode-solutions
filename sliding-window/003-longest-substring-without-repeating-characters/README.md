# Longest Substring Without Repeating Characters — LeetCode 3 (Medium)

**Pattern:** Sliding Window + Hash Set

## Problem
Given a string `s`, find the length of the longest substring without duplicate
characters. (A substring is contiguous — "pwke" from "pwwkew" does not count.)

## Examples
1. `s = "abcabcbb"` → `3` ("abc"; "bca" and "cab" also valid)
2. `s = "bbbbb"` → `1` ("b")
3. `s = "pwwkew"` → `3` ("wke")

## Constraints
- `0 <= s.length <= 10^5`
- `s` consists of English letters, digits, symbols and spaces.

## Approach
Keep a window `[left, right]` that only ever holds distinct characters, and a
set of what is inside it:

- Slide `right` forward one character at a time.
- If `s[right]` is already in the set, remove characters from the `left`
  until the duplicate is gone.
- Add `s[right]` and update the best length: `right - left + 1`.

The check only ever runs against the *current* window — a character that
already slid out of the window does not count as a repeat (that was the
"abba" trap: the last `a` is not a duplicate of the first `a`).

## Complexity
- Time: O(n) — every character is added to the set once and removed once.
- Space: O(min(n, alphabet)) — the set holds at most one window.

## Result (2026-11-23, user Jadu2049)
Accepted: **209 ms, beats 61.23%**; **19.83 MB, beats 66.91%**.
