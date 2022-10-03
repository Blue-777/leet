class Solution:
    def searchRange(self, num: List[int], target: int) -> List[int]:
    	return (lambda l,r: [-1,-1] if l == r else [l,r-1])(bisect.bisect_left(num,target),bisect.bisect(num,target))
		
	
