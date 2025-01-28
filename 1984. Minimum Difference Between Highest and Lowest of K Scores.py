class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left, right = 0, k - 1
        difference = float("inf")
        while right < len(nums):
            difference = min(difference, nums[right] - nums[left])
            left += 1
            right += 1
        return difference

# Intuition behind sorting and minimization?
# When you sort an array or list, the smaller numbers naturally move to the left, and the larger numbers shift to the right. This sorting helps because, in a sliding window, the difference between the maximum and minimum values within that window is minimized. Essentially, by having the numbers ordered, the smallest possible range of values (max - min) is more likely to occur, making it easier to find the minimum difference across the window.