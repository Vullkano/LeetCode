class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        x = abs(x)
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        if reversed_num > 2**31 - 1:
            return 0
        return sign * reversed_num