# Longest Consecutive Sequence — notes

Solved 2026-11-25 (LeetCode 128, Medium). Accepted 85/85, 43 ms, 36.49 MB.

## Approach (in your own words)
Put every number in a set. For each number, only start counting if
`num - 1` is not in the set — that means it is the start of a run.
Count forward from there and keep the longest run seen.

## Complexity
- Time: O(n) — each number is visited at most twice: once in the outer
  loop, once inside a run's forward count. The `num - 1` check is what
  keeps the inner loop from re-scanning the same run over and over.
- Space: O(n) — the set holds every distinct number once.

## What tripped me up / what I learned
- A loop inside a loop is not automatically O(n²). Here the inner
  `while` only ever walks numbers that belong to one run, and each
  number belongs to exactly one run — so the total work stays linear.
- Sorting first would also work, but it costs O(n log n) and breaks the
  problem's O(n) requirement. The set is what makes linear time possible.

## How it connects to Contains Duplicate
Same set, different job: Contains Duplicate used the set only to ask
"have I seen you before?"; here the set answers "are you here?" for
both the predecessor check and the forward walk, which is what lets
the runs be found without sorting.
