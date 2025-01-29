class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, next = 0, 0
        current_number = None
        while next < len(nums):
            if nums[next] != current_number:
                current_number = nums[next]
                nums[start], nums[next] = nums[next], nums[start]
                start += 1
            next += 1
        return start