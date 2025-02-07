class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            current = s[i]
            while i < j and s[i] == current:
                i += 1
            while i <= j and s[j] == current: # This <= is important (getting wrong ans if use < only)
                j -= 1
        return j - i + 1