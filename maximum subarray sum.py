# gfg - https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        curr_sum = 0
        max_len = 0
        prefix = 0
        hashmap = {0: -1}
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            prefix_sum = curr_sum - k
            
            if(prefix_sum in hashmap.keys()):
                max_len = max(max_len, i - hashmap[prefix_sum])
            
            if(curr_sum not in hashmap.keys()):
                hashmap[curr_sum] = i
        
        return max_len
    
if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")