class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr = 0
        for i in range(len(s)):
            if ptr < len(t) and s[i] == t[ptr]:
                ptr += 1
        return len(t) - ptr