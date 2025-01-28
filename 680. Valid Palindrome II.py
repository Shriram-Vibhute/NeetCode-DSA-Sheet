# The problem of this solution is the sequence that we are using to check the (s[left] != s[right]) is kind of wrong. because the test cases lilke (eceec and lcupuuuupcul) will fail.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        counter = 0
        while left < right and counter <= 1:
            if s[left] != s[right]:
                if s[left] == s[right - 1]:
                    counter += 1
                    right -= 1
                elif s[left + 1] == s[right]:
                    counter += 1
                    left += 1
                else:
                    print(s[left], " ", s[right])
                    return False
            left += 1
            right -= 1
        if counter <= 1:
            return True
        return False

# The 2nd approach - is directly checking the palendrome after the condition of skipping character 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if (s[left] != s[right]):
                skip_left_s = s[left + 1:right + 1]
                skip_right_s = s[left: right]
                # Either one of them must be palendrome

                return (skip_left_s == skip_left_s[::-1] or skip_right_s == skip_right_s[::-1])
            left += 1
            right -= 1
        return True