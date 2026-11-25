"""Group Anagrams — LeetCode 49 (Medium).

Anagrams share the same sorted letters, so sort each word and use that
as a key: "eat" and "tea" both become "aet" and land in the same bucket.

Run the tests:  python solution.py
"""

from collections import defaultdict


def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        # The sorted letters are the word's identity — same key, same group.
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def groupAnagrams(self, strs):
        return group_anagrams(strs)


def _same_groups(a, b):
    # Order of groups and order inside groups does not matter.
    return sorted(map(sorted, a)) == sorted(map(sorted, b))


if __name__ == "__main__":
    assert _same_groups(
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    )
    assert _same_groups(group_anagrams([""]), [[""]])
    assert _same_groups(group_anagrams(["a"]), [["a"]])
    assert _same_groups(group_anagrams(["abc", "bca", "xyz"]), [["abc", "bca"], ["xyz"]])
    print("All 4 tests passed.")
