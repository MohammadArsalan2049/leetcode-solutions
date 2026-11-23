# Notes — Longest Palindromic Substring (LeetCode 5)

## The one insight
Do not check every substring for being a palindrome (O(n^3)). Instead, pick
the center first and grow outward — a palindrome is defined by its center.

## Odd and even centers
Every string has 2n-1 centers: n characters (odd-length palindromes) and
n-1 gaps between characters (even-length palindromes). Missing the even
centers is the classic bug — `"cbbd"` has no odd palindrome longer than 1.

## The off-by-one in `expand`
When the while loop stops, `left` and `right` are one step *past* the
palindrome (they stopped because the characters did not match, or the edge
was reached). So the palindrome is `(left + 1, right - 1)`, not `(left, right)`.

## Tie-breaking
`>` instead of `>=` keeps the first longest palindrome found. Either answer
is accepted by LeetCode for `"babad"`.

## DP alternative (for later)
There is a DP version (table of "is s[i..j] a palindrome?") — same O(n^2)
time but O(n^2) space. Expand-around-center is strictly better here.
Manacher's algorithm does it in O(n), but that is an interview bonus, not
the expected answer.
