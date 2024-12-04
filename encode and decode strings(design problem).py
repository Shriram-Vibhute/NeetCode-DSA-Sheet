# Design Problem
class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i)) + "#" + i
        return ans

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while(i < len(s)):
            # Finding the index of j from i
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # Why only this way -> The length could be 2 digits like 10, 12
            i = j + 1
            word = ""
            for _ in range(i, i + length):
                word += s[i]
                i += 1
            res.append(word)
        return res