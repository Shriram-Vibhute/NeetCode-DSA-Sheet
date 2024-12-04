class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        curr_prod = 1
        # Forward pass
        for i in range(0, len(nums) - 1):
            curr_prod *= nums[i]
            ans[i + 1] = curr_prod
        print(ans)
        # Backword pass
        curr_prod = 1
        for i in range(len(nums) - 1, 0, -1):
            curr_prod *= nums[i]
            ans[i - 1] *= curr_prod
        return ans