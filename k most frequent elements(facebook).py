# leetcode - https://leetcode.com/problems/top-k-frequent-elements/
# Approach - Reversing bucket sort 
from typing import List, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = Counter(nums)
        hashing_list = [[] for i in range(len(nums) + 1)] # list of list
        
        for key in mpp.keys():
            hashing_list[mpp[key]].append(key)
        print(hashing_list)
        
        ans = []
        for i in range(len(hashing_list)-1, -1, -1):
            if(len(hashing_list[i]) <= 0): continue
            j = 0
            while(k != 0 and j < len(hashing_list[i])):
                ans.append(hashing_list[i][j])
                j += 1
                k -= 1
        return ans