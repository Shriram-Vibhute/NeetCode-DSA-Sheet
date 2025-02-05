class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        j = len(nums) - 1
        res = 0
        mod = 10 ** 9 + 7

        for i in range(len(nums)):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i <= j:
                res += ((2 ** (j - i)) % mod)
                res %= mod
        return int(res)