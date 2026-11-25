"""Top K Frequent Elements — LeetCode 347 (Medium).

Count frequencies, then bucket-sort by frequency: a number that appears
3 times goes in bucket 3. Read the buckets from the fullest down until
k numbers are collected — no sorting, no heap, O(n) time.

Run the tests:  python solution.py
"""

from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)
    # Max frequency is len(nums), so len(nums) + 1 buckets cover everything.
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(nums), 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def topKFrequent(self, nums, k):
        return top_k_frequent(nums, k)


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 1)) == [4]
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]
    print("All 4 tests passed.")
