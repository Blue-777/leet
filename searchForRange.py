class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        
        def searchLow(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
                
        def searchHigh(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        
        start = searchLow(nums, target)
        end = searchHigh(nums, target)
        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]