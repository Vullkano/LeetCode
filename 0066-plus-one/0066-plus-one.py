class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(0, len(digits)):
            iterador = len(digits) - 1
            lastNumber = digits[iterador - i]
            iterador -= i
            if lastNumber == 9:
                digits[iterador] = 0
                if digits[0] == 0:
                    digits.insert(0, 1)
                    return digits
            elif lastNumber != 9:
                digits[iterador] += 1
                return digits
