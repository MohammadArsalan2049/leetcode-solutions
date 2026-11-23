# Add Two Numbers — LeetCode 2 (Medium)

**Pattern:** Linked List + Simulation (school addition, column by column)

## Problem
You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each node contains a single digit. Add the
two numbers and return the sum as a linked list.

## Examples
1. `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]` → `[7, 0, 8]` (342 + 465 = 807)
2. `l1 = [0]`, `l2 = [0]` → `[0]`
3. `l1 = [9, 9, 9, 9, 9, 9, 9]`, `l2 = [9, 9, 9, 9]` → `[8, 9, 9, 9, 0, 0, 0, 1]`

## Constraints
- `1 <= length of each list <= 100`
- `0 <= Node.val <= 9`
- No leading zeros, except the number 0 itself.

## Approach
The digits are stored in reverse, so the head of the list is the ones place.
Add them exactly like school addition, left to right, carrying over:

- Walk both lists together with a `carry` (starts at 0).
- At each step: `total = (l1 digit or 0) + (l2 digit or 0) + carry`;
  new digit = `total % 10`, new carry = `total // 10`.
- Keep going while either list has digits **or** a carry is left over —
  that final carry is the extra `1` in example 3.
- Build the answer with a **dummy head node** so the first node is not a
  special case; return `dummy.next`.

## Complexity
- Time: O(max(m, n)) — one pass over the longer list.
- Space: O(max(m, n)) — the answer list.

## Result (2026-11-23, user Jadu2049)
Accepted: **3 ms, beats 76.48%**; **19.13 MB, beats 80.76%**.
