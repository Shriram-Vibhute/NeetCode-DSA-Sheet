from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.array = []
        sum = 0
        for num in nums:
            sum += num
            self.array.append(sum)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.array[right] - self.array[left - 1] if left > 0 else self.array[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)