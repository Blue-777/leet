class Solution:
    	def nextGreatestLetter(self, letters: List[str], target: str) -> str:
		for i in letters:
			if i>target:
				return i
			if letters[-1]<=target:
				return letters[0]