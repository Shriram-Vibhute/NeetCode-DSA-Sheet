# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
class Solution:
    def minSwaps(self, s: str) -> int:
        ct, mx = 0, 0
        for i in range(len(s)):
            ct = ct + 1 if s[i] == ']' else ct - 1
            mx = max(mx, ct)
        return int((mx + 1) / 2)