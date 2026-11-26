# Implement Queue using Stacks — notes

Solved 2026-11-26 (LeetCode 232, Easy). Accepted 23/23, 0 ms, 19.13 MB.

## Approach (in your own words)
I used two stacks. Everything new goes on the in-stack. When I need
to pop or peek and the out-stack is empty, I pour the whole in-stack
into the out-stack — that flips the order, so the oldest element ends
up on top and comes out first, just like a queue. I only pour when the
out-stack is empty, so each element moves at most twice.

## Complexity
- Time: push O(1); pop and peek are amortized O(1) — the pour costs
  O(n) when it happens, but each element is poured at most once, so
  the cost spreads out over the operations.
- Space: O(n) — the two stacks together hold every element once.

## What tripped me up / what I learned
- The pour is the whole trick: one stack reverses order, and
  reversing twice brings it back. The in-stack holds elements
  newest-first; pouring them into the out-stack makes them
  oldest-first, which is exactly what a queue needs.
- Pouring lazily matters. If I poured on every pop, every pop would
  cost O(n). Pouring only when the out-stack is empty is what makes
  the amortized cost O(1).
- Unlike the other problems, there is no `Solution` class here —
  LeetCode tests the `MyQueue` class itself, so the class I wrote
  is the answer.
