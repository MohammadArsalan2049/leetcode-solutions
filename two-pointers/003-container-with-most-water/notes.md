# Container With Most Water — notes

Solved 2026-11-28 (LeetCode 11, Medium). Accepted 65/65, 58 ms, 29.53 MB.

## Approach (in your own words)
I used two pointers, one at each end of the array. The area between
them is the shorter line's height times the distance between them,
so I track the biggest area I see. Then I move the pointer at the
shorter line inward — the shorter line is what limits the area, so
moving the taller one instead could only shrink the width without
raising the limit. I keep going until the pointers meet.

## Complexity
- Time: O(n) — each pointer moves across the array at most once.
- Space: O(1) — no extra storage, just the two pointers and the
  best area so far.

## What tripped me up / what I learned
- The move is the whole problem: it feels wrong to throw away the
  shorter line, but every container using it with a line further in
  is narrower and capped at the same height or less, so nothing is
  lost by moving past it.
- This is the same two-pointer shape as Two Sum II — pointers at
  both ends, move one side based on a comparison — but the decision
  here is about which line limits the area, not about a sum.
- The brute force checks every pair, O(n²). The two-pointer version
  checks each line at most once and is already optimal.
