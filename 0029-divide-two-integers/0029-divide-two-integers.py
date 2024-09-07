class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) == 1:
            return min(2 ** 31 - 1, max(-2 ** 31, dividend * divisor))

        sinal = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        resultado = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            resultado += multiple

        resultado *= sinal

        return min(2 ** 31 - 1, max(-2 ** 31, resultado))