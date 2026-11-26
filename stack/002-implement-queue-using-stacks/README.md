# Implement Queue using Stacks — LeetCode 232 (Easy)

**Pattern:** Stack (Stage 6 of the starter guide — second stack problem)

## Problem
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:
- `MyQueue()` — initializes the queue object.
- `void push(int x)` — pushes element `x` to the back of the queue.
- `int pop()` — removes the element from the front of the queue and returns it.
- `int peek()` — returns the element at the front of the queue.
- `boolean empty()` — returns `true` if the queue is empty, `false` otherwise.

You must use only standard stack operations: push to top, peek/pop from top, size, and is empty.

## Example
- Input: `["MyQueue", "push", "push", "peek", "pop", "empty"]`, `[[], [1], [2], [], [], []]`
- Output: `[null, null, null, 1, 1, false]`
- Explanation: `MyQueue myQueue = new MyQueue(); myQueue.push(1); myQueue.push(2); myQueue.peek(); // returns 1; myQueue.pop(); // returns 1; myQueue.empty(); // returns false`

## Constraints
- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

## Hints (read one at a time — try before reading the next)
1. **The mismatch:** a stack gives you the newest element first; a queue must give you the oldest first. What happens if you pour one stack into another?
2. **The tool:** two stacks — one for incoming elements, one for outgoing. When is the pour needed?
3. **The lazy trick:** only pour when the out-stack is empty. Why does that keep every operation cheap?

## Before you code (1-minute checklist from the guide)
- What pattern is this? What are the inputs/outputs?
- What is the brute-force answer, and its Big O?
- What is the edge case? (Popping or peeking when the queue has one element left.)

## Result (2026-11-26, user Jadu2049)
Accepted: **23/23 test cases; 0 ms, beats 100.00%**; **19.13 MB, beats 95.61%**.
Solved with two stacks: push onto the in-stack, pour into the out-stack only when it is empty, and pop/peek from the out-stack.
