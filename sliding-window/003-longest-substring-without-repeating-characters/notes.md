# Notes — Longest Substring Without Repeating Characters (LeetCode 3)

## The one insight
A substring is a *window*. Instead of checking every possible substring
(O(n^2)), keep one window that is always valid (no repeats) and slide it.

## Why `while`, not `if`
When the new character is a duplicate, one removal from the left is not
always enough. In `"abcabcbb"`, when `right` reaches the second `b` (index 6),
you must drop `a` *and* `b` before the window is clean again.

## The "abba" trap
Checking the new character against *all* previous characters (from index 0)
is wrong: the first `a` in `"abba"` is already outside the window when the
last `a` arrives. The check must run only from `left` to `right - 1`.
The set does exactly this — it only holds the current window.

## Brute force vs this
Brute force (two nested loops, checking every substring) is O(n^2) and times
out at n = 10^5. The set gives O(1) duplicate checks, so the whole thing is
O(n).

## A faster variant (for later)
A dict storing each character's *last seen index* lets you jump `left`
straight to `last_index + 1` instead of shrinking one by one. Same O(n),
fewer steps — worth knowing, not needed here.
