# Two Sum II — notes

Solved 2026-11-28 (LeetCode 167, Easy). Accepted 26/26, 7 ms, 22.51 MB.

## Approach (in your own words)
I used two pointers, one at each end of the sorted array. I add the
two numbers the pointers sit on: if the sum is smaller than the
target, the left pointer has to move right to make the sum bigger;
if the sum is bigger than the target, the right pointer has to move
left to make it smaller. When the sum matches, I return the two
positions — plus 1 on each, because the answer is 1-indexed.

## Complexity
- Time: O(n) — each pointer moves across the array at most once.
- Space: O(1) — no extra storage, just the two pointers.

## What tripped me up / what I learned
- This is the same question as Two Sum, but the sorted input changes
  everything: a hash map works too, but two pointers solve it in
  O(1) space because sorted order tells you which way to move.
- The 1-indexed answer is the trap in this problem — the pointers
  are 0-indexed, so forgetting the +1 on each side gives the wrong
  answer even when the logic is right.
- Beats percentages are noisy and not a grade: 7 ms beats 57.31%
  and the memory beats 18.60%, but the solution is already optimal
  at O(n) time and O(1) space, so there is nothing to chase here.
