# Contains Duplicate — notes

Solved 2026-11-23 (LeetCode 217, Easy).

## Approach (in your own words)
Walk the list once with a set of numbers seen so far. For each number, ask
"have I seen you before?" — if yes, return `True` on the spot; if no, add it
to the set and keep going. If the loop finishes, every element was distinct,
so return `False`.

## Complexity
- Time: O(n) — one pass; each set lookup and add is O(1) on average.
- Space: O(n) — the set holds up to one copy of each distinct value.

## What tripped me up / what I learned
- Check **before** adding: `if num in seen` must come before `seen.add(num)`,
  otherwise every number "finds itself" and the answer is always `True`.
- The early `return True` means the loop often stops before the end of the
  list — no need to scan the rest once a repeat is found.
- One-liner version: `len(set(nums)) != len(nums)` — a set keeps only one
  copy of each value, so a smaller set means a duplicate existed. It works,
  but it always builds the whole set first; the loop version exits early.

## How it connects to Two Sum
Same hash-lookup idea, simpler job: Two Sum's dict remembers *where* each
value was (index) so it can return the pair; here a set only remembers
*whether* a value was seen, because the question is only true/false.
