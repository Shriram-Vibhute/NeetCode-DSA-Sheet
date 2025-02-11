# Prefix Sum Logic
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        ans = 0
        counter_1, counter_0 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter_0 += 1
            else:
                counter_1 += 1

            diff = counter_1 - counter_0
            if diff not in hashmap.keys():
                hashmap[diff] = i
            
            if counter_0 == counter_1:
                ans = counter_0 + counter_1
            else:
                ans = max(ans, i - hashmap[diff])

        return ans