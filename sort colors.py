class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, ptr = 0, len(nums)-1, 0
        while(ptr <= j):
            if(nums[ptr] == 0):
                nums[i], nums[ptr] = nums[ptr], nums[i]
                i += 1
                ptr += 1
            
            elif(nums[ptr] == 2):
                nums[j], nums[ptr] = nums[ptr], nums[j]
                j -= 1
            
            else:
                ptr += 1
                
        