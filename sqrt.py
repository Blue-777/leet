class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l + 1 < r:
            m = (l+r)//2
            if m * m > x: r = m 
            if m * m < x: l = m
            if m * m == x: return int(m)

        if r * r == x: return int(r)
        return int((l+r)/2)
        