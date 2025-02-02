class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()

        for i in range(0, len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    # if [nums[i], nums[j], nums[k]] not in result:
                    #     result.append([nums[i], nums[j], nums[k]]) -> This will give a TLE
                    result.append([nums[i], nums[j], nums[k]])
                    num_j, num_k = nums[j], nums[k]
                    while j < len(nums) and nums[j] == num_j:
                        j += 1
                    while k > -1 and nums[k] == num_k:
                        k -= 1                   
        return result