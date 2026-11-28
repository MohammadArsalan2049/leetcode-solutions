# 3Sum — notes

Solved 2026-11-28 (LeetCode 15, Medium). Accepted 316/316, 650 ms, 22.08 MB.

## Approach (in your own words)
I sort the array first, then fix one number at a time. For each
fixed number I use two pointers on the rest to find pairs that add
up to its negative, exactly like Two Sum II. The duplicate handling
is the whole problem: I skip the same value for the fixed index, and
after finding a triplet I skip past any repeated values on both
pointers before looking for the next one.

## Complexity
- Time: O(n²) — sorting is O(n log n), then for each of the n
  fixed positions the two pointers scan at most n elements.
- Space: O(1) extra, besides the output list itself.

## What tripped me up / what I learned
- Sorting first is what makes this solvable with two pointers — the
  same trick as Two Sum II, just with one extra fixed number.
- The duplicates are where this problem bites: without skipping
  them, the same triplet comes out many times. All three positions
  need their own skip, not just one.
- 650 ms beats 48.59%, and that is fine — O(n²) is the expected
  answer for 3Sum, and the beats percentage is a noisy percentile,
  not a grade.
