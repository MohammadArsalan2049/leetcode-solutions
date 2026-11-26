# Valid Palindrome — notes

Solved 2026-11-26 (LeetCode 125, Easy). Accepted 492/492, 9 ms, 19.40 MB.

## Approach (in your own words)
I used two pointers, one at each end of the string. Both skip
anything that is not a letter or digit, then I compare the two
characters in lowercase. If they ever differ, it is not a palindrome.
If the pointers meet without a mismatch, it is.

## Complexity
- Time: O(n) — each character is visited at most once by the
  pointers.
- Space: O(1) — no cleaned copy of the string is built; the check
  happens on the original string.

## What tripped me up / what I learned
- The beats percentage dropped to 47.82% on this one, and that is
  fine — it is a noisy percentile, not a grade. The solution is
  already optimal: O(n) time and O(1) space, and there is no faster
  way to check a string you have to read fully.
- The first instinct is to clean the string into a new one and then
  compare it with its reverse. That works, but it costs O(n) extra
  space. The two-pointer version does the skipping and the comparing
  in the same pass.
- A string of only spaces or punctuation is a palindrome — after
  removing everything non-alphanumeric there is nothing left, and
  the pointers just meet.
