# Best Time to Buy and Sell Stock — LeetCode 121 (Easy)

**Pattern:** Sliding Window / Greedy (Stage 2 of the starter guide)

## Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Examples
1. `prices = [7, 1, 5, 3, 6, 4]` → `5` (buy on day 2 at 1, sell on day 5 at 6)
2. `prices = [7, 6, 4, 3, 1]` → `0` (no profit possible)

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Hints (read one at a time — try before reading the next)
1. **The brute force trap:** checking every buy day against every later sell day works, but it is O(n²). Can one pass do it?
2. **The one thing to remember:** the lowest price seen so far. Today's profit is today's price minus that lowest price.
3. **The order is free:** selling always comes after buying, because the single pass only ever looks back at prices already seen.

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (Prices only falling — answer 0, never negative.)

## Result (2026-11-28, user Jadu2049)
Accepted: **213/213 test cases; 40 ms, beats 71.29%**; **29.18 MB, beats 7.21%**.
Solved in one pass tracking the lowest price so far and the best profit seen.
