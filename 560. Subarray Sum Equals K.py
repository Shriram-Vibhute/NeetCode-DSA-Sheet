# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        hashmap = {0: 1} # Rather than storing the index - sum we have to store count - sum

        for i in range(len(nums)):
            sum += nums[i]
            prefix_sum = sum - k

            if prefix_sum in hashmap.keys():
                count += hashmap[prefix_sum]

            if sum in hashmap.keys(): hashmap[sum] += 1
            else: hashmap[sum] = 1
        
        return count