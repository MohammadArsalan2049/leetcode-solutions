# Valid Parentheses — LeetCode 20 (Easy)

**Pattern:** Stack (Stage 6 of the starter guide — first stack problem)

## Problem
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
1. `s = "()"` → `true`
2. `s = "()[]{}"` → `true`
3. `s = "(]"` → `false`
4. `s = "([)]"` → `false`
5. `s = "{[]}"` → `true`

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`.

## Hints (read one at a time — try before reading the next)
1. **The order matters:** a closing bracket must match the *most recent* unclosed opening bracket. What data structure always gives you the most recent thing first?
2. **The tool:** a stack. Push openings, and on a closing bracket check the top.
3. **The two failure cases:** a closing bracket that does not match the top (or arrives with an empty stack), and a stack that is not empty when the string ends.

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (A single opening bracket, and a closing bracket first.)

## Result (2026-11-26, user Jadu2049)
Accepted: **103/103 test cases; 0 ms, beats 100.00%**; **18.94 MB, beats 98.13%**.
Solved with the stack approach: push openings, match each closing bracket against the top of the stack, and require an empty stack at the end.
