class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[(k + i) % len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = ans[i]
        # nums = ans -> This will not change all the varuables inplace it will just creats a new referance (ChatGPT)