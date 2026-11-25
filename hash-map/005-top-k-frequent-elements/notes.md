# Top K Frequent Elements — notes

Solved 2026-11-25 (LeetCode 347, Medium). Accepted 26/26, 10 ms, 24.71 MB.

## Approach (in your own words)
Count how many times each number appears, then bucket-sort by
frequency: a number appearing 3 times goes in bucket 3. The most
frequent count cannot exceed n, so n + 1 buckets cover everything.
Read the buckets from the fullest down and stop as soon as k numbers
are collected.

## Complexity
- Time: O(n) — one pass to count, one pass to fill buckets, one pass down the buckets. No sorting, no heap.
- Space: O(n) — the counter plus the buckets hold every number once.

## What tripped me up / what I learned
- The follow-up rules out sorting by frequency (O(n log n)). Bucket
  sort is the trick that keeps it linear: the frequency itself is the
  index, so placing a number costs O(1).
- "Beats %" is noisy and not a grade: it compares your run against
  every accepted submission ever, and LeetCode's timing varies run to
  run — the same code can show a different beats % on a second submit.
  This solution is O(n), the best possible complexity for this problem;
  a heap version is O(n log k) and only looks faster on the board by luck.

## How it connects to Valid Anagram and Group Anagrams
Same frequency-counting family, new ranking step: Valid Anagram counted
letters to compare two strings, Group Anagrams used a key to bucket
words, and here the frequency itself becomes the bucket index — the
count is not just checked, it is used to order the answer.
