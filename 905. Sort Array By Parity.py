class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start, next = 0, 0
        while next < len(nums):
            if nums[next] % 2 == 0:
                nums[next], nums[start] = nums[start], nums[next]
                start += 1
            next += 1
        return nums