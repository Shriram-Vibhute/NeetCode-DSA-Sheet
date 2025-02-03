class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    curr_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if curr_sum < target:
                        start += 1
                    elif curr_sum > target:
                        end -= 1
                    else:
                        # print(nums[i], nums[j], nums[start], nums[end])
                        # print(i, j, start, end)
                        ans.append([nums[i], nums[j], nums[start], nums[end]])
                        num_start = nums[start]
                        num_end = nums[end]
                        while start < len(nums) and nums[start] == num_start:
                            start += 1
                        while start < end and nums[end] == num_end:
                            end -= 1
                num_j = nums[j]
                while j < len(nums) and num_j == nums[j]:
                    j += 1
            num_i = nums[i]
            while i < len(nums) and num_i == nums[i]:
                i += 1
        return ans