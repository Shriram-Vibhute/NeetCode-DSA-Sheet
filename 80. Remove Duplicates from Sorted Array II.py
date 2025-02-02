class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, next = 0, 0
        counter = 0
        curr_elem = None

        while next < len(nums):
            if nums[next] != curr_elem:
                curr_elem = nums[next]
                counter = 1
                nums[start], nums[next] = nums[next], nums[start]
                start += 1
            else:
                if counter < 2:
                    nums[start], nums[next] = nums[next], nums[start]
                    counter += 1
                    start += 1
            next += 1

        return start