class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        
        i = 0
        max_len = 0
        while(i < len(nums)):
            current_number = nums[i]
            if((nums[i] - 1) not in hashset):
                next_number = current_number + 1
                curr_len = 1
                while(next_number in hashset):
                    next_number += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
            i += 1
        
        return max_len
        