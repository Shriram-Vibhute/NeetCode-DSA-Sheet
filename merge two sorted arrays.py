def merge(start: int, mid: int, end: int, nums: List[int]) -> List[int]:
    store = list()
    ptr1 = start
    ptr2 = mid + 1

    while(ptr1 != mid + 1 and ptr2 != end + 1):
        if(nums[ptr1] < nums[ptr2]):
            store.append(nums[ptr1])
            ptr1 += 1
        else:
            store.append(nums[ptr2])
            ptr2 += 1
    
    while(ptr1 != mid + 1):
        store.append(nums[ptr1])
        ptr1 += 1
    
    while(ptr2 != end + 1):
        store.append(nums[ptr2])
        ptr2 += 1
    
    for i in range(len(store)):
        nums[i + start] = store[i]

    return nums    

def merge_sort(nums: List[int], start, end):
    # Base Condition
    if(start == end):
        return nums
    
    # Recursion Operation
    mid = start + (end - start) // 2

    merge_sort(nums, start, mid)
    merge_sort(nums, mid + 1, end)

    return merge(start, mid, end, nums)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums, 0, len(nums) - 1)