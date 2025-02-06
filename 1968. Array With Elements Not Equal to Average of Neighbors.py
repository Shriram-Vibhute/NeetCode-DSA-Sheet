class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        left, right = 0, len(nums) - 1
        res = []

        while len(nums) != len(res):
            res.append(nums[left])
            left += 1

            if right > left:
                res.append(nums[right])
                right -= 1

        return res 