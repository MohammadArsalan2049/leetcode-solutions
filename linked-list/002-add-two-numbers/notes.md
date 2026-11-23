# Notes — Add Two Numbers (LeetCode 2)

## The one insight
Reverse order is a gift, not a trap: the head is the ones place, so plain
column addition works left to right. If the digits were stored forwards,
you would have to reverse the lists first (or use a stack).

## The line doing the most work
`while l1 or l2 or carry:` — it handles three cases at once:
1. both lists still have digits,
2. the lists are different lengths (a missing digit counts as 0),
3. a carry is left over after both lists end (the extra `1` in example 3).

## The dummy-node trick
`dummy = ListNode(0)`, build on `curr`, return `dummy.next`. Without it,
the first answer node needs its own special case. Same trick appears in
most linked-list construction problems — remember it.

## Mistakes to avoid
- Forgetting the final carry (`[5] + [5]` must give `[0, 1]`, not `[0]`).
- Advancing `l1`/`l2` without checking they exist (lists have different lengths).
- Returning `dummy` instead of `dummy.next` (extra leading 0).
