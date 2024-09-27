class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        FinalList = []
        for i in digits:
            number += str(i)
        number = str(int(number) + 1)
        for i in number:
            FinalList.append(int(i))
        return FinalList
