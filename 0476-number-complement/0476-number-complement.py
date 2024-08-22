class Solution:
    def findComplement(self, num: int) -> int:
        mid = num.bit_length()  # Número de algarismos do num em binário
        mask = (2**mid) - 1  # Ou: 1 << mid
        return mask ^ num  # Operação XOR