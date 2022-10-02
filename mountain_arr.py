class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0 
        index_pos = 0 
        while(i < len(arr) -1):
            if arr[i] < arr[i + 1]:
                index_pos += 1
            else:
                return index_pos
            i += 1