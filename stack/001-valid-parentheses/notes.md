# Valid Parentheses — notes

Solved 2026-11-26 (LeetCode 20, Easy). Accepted 103/103, 0 ms, 18.94 MB.

## Approach (in your own words)
I used a stack. Every opening bracket gets pushed, and when a closing
bracket shows up I check it against the top of the stack — it has to be
the matching type, or the string is invalid. If the stack is empty when
a closer arrives, that is invalid too. At the end the stack has to be
empty, otherwise something was never closed.

## Complexity
- Time: O(n) — one pass over the string, and every bracket is pushed
  and popped at most once.
- Space: O(n) — in the worst case (all opening brackets) the stack
  holds the whole string.

## What tripped me up / what I learned
- The key insight is that the *most recent* unclosed bracket is the
  one that has to close next, and a stack is exactly the structure
  that hands you the most recent thing first.
- `"([)]"` is the classic trap: every bracket type appears and every
  type is closed, but the order is wrong — the `)` arrives while `[`
  is on top, so it fails. Counting brackets is not enough; order is
  the whole problem.
- This is my first stack problem — the hash-map stage is done, and
  the stack is the next pattern in the guide.
