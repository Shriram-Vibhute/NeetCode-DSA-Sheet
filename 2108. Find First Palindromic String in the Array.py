def isPalendrome(s: str) -> bool:
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if isPalendrome(s):
                return s
        return ""    