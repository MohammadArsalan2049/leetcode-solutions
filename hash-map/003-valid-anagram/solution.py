"""Valid Anagram — LeetCode 242 (Easy).

Two strings are anagrams when they have the same letters with the same
counts. Count the letters of `s` once, then spend one count per letter
of `t` — the moment a letter is missing or used up, it is not an anagram.

Run the tests:  python solution.py
"""


def is_anagram(s, t):
    # Quick reject: different lengths can never be anagrams.
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        # Missing letter, or already spent all copies of it.
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    return True


class Solution:
    """LeetCode entry point — same logic, LeetCode's class shape."""

    def isAnagram(self, s, t):
        return is_anagram(s, t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "bello") is False
    assert is_anagram("a", "a") is True
    assert is_anagram("ab", "a") is False
    print("All 6 tests passed.")
