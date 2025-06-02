def dfs(nums, i, total):
    # Stopping Condition
    if i == len(nums):
        return total
    
    # Taking the current number
    take_result = dfs(nums, i + 1, total ^ nums[i])
    # Not taking the current number
    nontake_result = dfs(nums, i + 1, total)

    # Addition of both the components
    return take_result + nontake_result

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return dfs(nums, 0, 0)