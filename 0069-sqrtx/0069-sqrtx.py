class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        elif x < 6:
            return x // 2
        high = x // 2
        low = -1
        mid = high // 2
        if high * high == x:
            return high
        while low + 1 != mid or mid != high - 1:
            if mid * mid > x:
                high = mid
                mid = high // 2
            elif mid * mid < x:
                low = mid
                mid = int((low + high)/2)
            else:
                return mid
        if mid * mid > x:
            return low
        return mid