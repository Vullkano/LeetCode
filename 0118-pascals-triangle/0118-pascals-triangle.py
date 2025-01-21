class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        import math
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        listafinal  = []
        for n in range(numRows):
            lista = []
            for p in range(n + 1):
                lista.append(int(math.factorial(n)/(math.factorial(p)*(math.factorial(n-p)))))
            listafinal.append(lista)
        return listafinal