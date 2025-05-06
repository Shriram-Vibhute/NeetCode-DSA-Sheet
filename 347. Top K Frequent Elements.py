# Approach 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Storing the frequency
        hashset = defaultdict(int)
        for num in nums:
            hashset[num] += 1
        
        # Sorting the values
        sorted_freqs = sorted(hashset.values())[len(hashset) - k:]

        # Finding the values in hashset
        res = []
        for key, val in hashset.items():
            if val in sorted_freqs:
                res.append(key)
        
        return res

# Approach 2 - Reverse Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Storing the hash
        freq = [[] for i in range(len(nums) + 1)] # list of list
        hashmap = defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1

        # looping
        for key in hashmap.keys():
            freq[hashmap[key]].append(key)

        res = []
        for arr in freq[::-1]:
            j = 0
            while(k != 0 and j < len(arr)):
                res.append(arr[j])
                j += 1
                k -= 1
        
        return res 