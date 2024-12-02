# leetcode - https://leetcode.com/problems/two-sum/
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            prefix_num = abs(nums[i] - target)
            if(prefix_num in hashmap.keys()):
                return [i, hashmap[prefix_num]]
            else:
                hashmap[nums[i]] = i
        return [0]

if __name__ == "__main__":
    solution = Solution()
    nums = input("Enter your list : ").split(' ')
    print(solution.twoSum(nums))