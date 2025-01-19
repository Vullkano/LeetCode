class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        verificar = ""
        longo = 0
        for letra in s:
            if letra not in verificar:
                verificar += letra
                longo = max(longo, len(verificar))
            else:
                if verificar[-1] == letra:
                    verificar = letra
                else:
                    verificar = verificar[verificar.index(letra)+1:] + letra
        return longo