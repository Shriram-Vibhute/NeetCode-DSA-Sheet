class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        overall_max = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            print(i)
            curr = arr[i]
            arr[i] = overall_max
            overall_max = max(curr, overall_max)
        arr[-1] = -1
        return arr