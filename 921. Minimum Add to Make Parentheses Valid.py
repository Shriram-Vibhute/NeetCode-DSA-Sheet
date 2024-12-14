# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/ - Using Stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ct = []
        for i in range(len(s)):
            if s[i] == ')' and len(ct) != 0 and ct[-1] == '(':
                ct.pop()
                continue
            ct.append(s[i])
        return len(ct)