# Two Sum — notes

Solved 2026-11-14, first LeetCode problem. Accepted: 66/66 test cases, 0 ms (beats 100%), 20.32 MB.

## Approach (in your own words)
For each number, work out the partner it needs: `needed = target - num`.
Keep a dict of numbers seen so far and their indices. If the needed
partner is already in the dict, return its index and the current index.
Check before storing, so the same element is never used twice.

## Complexity
- Time: O(n) — one pass through the list.
- Space: O(n) — the dict stores the numbers seen.

## What tripped me up / what I learned
- First attempt was C++ brute force (check every pair) with errors:
  `num.length` instead of `nums.size()`, `i`/`j` undeclared, and
  `print(i, j)` instead of returning the answer.
- Pasted the Python solution into the C++ editor first and got
  "expected class name" — the fix is switching LeetCode's language
  dropdown to Python3 before pasting.
- Python is the language for this practice going forward.
