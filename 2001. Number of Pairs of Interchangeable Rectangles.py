# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/ - Easy problem - compinations
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashmap = {}
        total = 0
        for i in range(len(rectangles)):
            ratio = rectangles[i][0] / rectangles[i][1]
            if ratio not in hashmap.keys():
                hashmap[ratio] = [i]
            else:
                hashmap[ratio].append(i)
        
        print(hashmap)
        
        # Permutation
        for i in hashmap.values():
            length, ans = len(i), 1
            if(length > 1):
                ans = length * (length - 1) / 2
                total += ans

        return int(total)