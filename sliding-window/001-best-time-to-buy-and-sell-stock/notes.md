# Best Time to Buy and Sell Stock — notes

Solved 2026-11-28 (LeetCode 121, Easy). Accepted 213/213, 40 ms, 29.18 MB.

## Approach (in your own words)
I walk through the prices once, remembering the lowest price I have
seen so far. For each day, the profit if I sold today is today's
price minus that lowest price, and I keep the best profit I have
seen. If today's price is lower than everything before it, it
becomes the new lowest price to buy at.

## Complexity
- Time: O(n) — one pass through the prices.
- Space: O(1) — just the lowest price and the best profit.

## What tripped me up / what I learned
- The buy-before-sell rule looks like it needs checking, but the
  single pass gives it for free: the lowest price is always from a
  day already passed, so any profit I compute sells after buying.
- The answer is never negative — if prices only fall, the best
  profit stays 0 instead of going below zero.
- The memory beats 7.21% looks bad, but it is just Python's
  overhead on this problem, not the algorithm: the solution uses
  O(1) extra space, which is already optimal.
