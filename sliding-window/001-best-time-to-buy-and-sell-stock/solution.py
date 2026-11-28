"""Best Time to Buy and Sell Stock — LeetCode 121 (Easy).

One pass: remember the lowest price seen so far. Today's profit is
today's price minus that lowest price; keep the best profit seen.
Selling always comes after buying because the pass only looks back.
O(n) time, O(1) extra space.

Run the tests:  python solution.py
"""


def max_profit(prices):
    min_price = prices[0]
    best = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            best = max(best, price - min_price)
    return best


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def maxProfit(self, prices):
        return max_profit(prices)


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1]) == 0
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4
    print("All 5 tests passed.")
