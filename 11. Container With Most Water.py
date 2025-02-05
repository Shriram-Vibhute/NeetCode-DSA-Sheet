class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            area = max(area, current_area)

            # Moving pointers
            if height[left] < height[right]:
                left += 1
            else :
                right -= 1
        
        return area

# What I Learned from this question - If two pointer is applied without sorting you must increase / decrease towards continuois minium or maxium element according to question