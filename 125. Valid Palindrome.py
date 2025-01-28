class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 Pointer Approach without using space
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            # If left is not alpha - numaric
            if s[left].isalnum() == False:
                left += 1
                continue
            elif s[right].isalnum() == False:
                right -= 1
                continue
            else:
                # They both are alpha numeric
                if(s[left] != s[right]):
                    return False
                left += 1
                right -= 1
        return True