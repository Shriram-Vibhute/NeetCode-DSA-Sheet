class Solution:
    def scoreOfString(self, s: str) -> int:
        i, j = 0, 1
        total_sum = 0
        while j < len(s):
            total_sum += abs(ord(s[i]) - ord(s[j]))
            i += 1
            j += 1
        return total_sum