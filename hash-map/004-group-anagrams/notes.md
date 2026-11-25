# Group Anagrams — notes

Solved 2026-11-25 (LeetCode 49, Medium). Accepted 130/130, 12 ms, 21.72 MB.

## Approach (in your own words)
Anagrams share the same sorted letters, so sort each word and use that
as a key. Walk the list once, put each word in the bucket for its key,
then return the buckets. `defaultdict(list)` means a missing key starts
as an empty list, so you can append straight away.

## Complexity
- Time: O(n · k log k) — n words, sorting each word of length k costs k log k.
- Space: O(n · k) — the dict holds every word once, plus its sorted key.
- Faster key: counting the letters into a 26-length tuple gives O(n · k)
  with no sorting, but the sorted key is simpler and fast enough here.

## What tripped me up / what I learned
- The answer's order does not matter — LeetCode accepts the groups in
  any order, and the words inside a group in any order too.
- The sorted word is the word's "identity": two words are anagrams
  exactly when their sorted forms are equal.

## How it connects to Valid Anagram
Same idea, bigger job: Valid Anagram asked whether two strings share an
identity; here every word gets its identity as a key, and the dict
groups all the words that share one. The dict goes from remembering
counts (Valid Anagram) to remembering whole groups of words.
