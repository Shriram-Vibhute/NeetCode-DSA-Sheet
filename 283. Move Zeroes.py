class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start, next = 0, 0

        while next < len(nums):
            if nums[start] != 0: 
                start+=1
                next = start + 1
                continue
            else:
                nums[start], nums[next] = nums[next], nums[start]
                next+=1