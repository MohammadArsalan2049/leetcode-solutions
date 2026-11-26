"""Implement Queue using Stacks — LeetCode 232 (Easy).

Two stacks make a queue: new elements go on the in-stack, and when
the out-stack is empty it gets filled by pouring the in-stack over —
that reverses the order, so the oldest element ends up on top.
Each element moves at most twice, so pop/peek are amortized O(1).

Run the tests:  python solution.py
"""


class MyQueue:
    """LeetCode entry point — the queue itself is the solution."""

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True
    q.push(3)
    assert q.peek() == 3
    assert q.pop() == 3
    assert q.empty() is True
    print("All 8 tests passed.")
