class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i, val in enumerate(arr):
            if arr[i + 1] < arr[i]:
                return i