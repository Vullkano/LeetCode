class Solution:
    def myAtoi(self, s: str) -> int:
        number = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        x = False
        pontuation = 1

        def rounding(x):
            if x > 2**31 - 1:
                return 2**31 - 1
            elif x < -2**31:
                return -2**31
            return x

        for i in s:
            if i in number:
                x = x * 10 + number[i]
            elif i == " ":
                if type(x) != bool:
                    return rounding(x * pontuation)
                pass
            elif i == "+":
                if type(x) != bool:
                    return rounding(x * pontuation)
                x += 0
            elif i == "-":
                if type(x) != bool:
                    return rounding(x * pontuation)
                pontuation *= -1
                x += 0
            else:
                return rounding(x * pontuation)
        return rounding(x * pontuation)