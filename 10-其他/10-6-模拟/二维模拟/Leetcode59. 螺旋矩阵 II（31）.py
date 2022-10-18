class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]
        count = n * n
        left, right, top, buttom = 0, n-1, 0, n-1
        matrix = [[0 for _ in range(n)]for _ in range(n)]
        cur = 1
        while cur <= count:
            for i in range(left, right+1):
                matrix[top][i] = cur
                cur += 1
            top += 1
            for i in range(top, buttom+1):
                matrix[i][right] = cur
                cur += 1
            right -= 1
            for i in range(right, left-1, -1):
                matrix[buttom][i] = cur
                cur += 1
            buttom -= 1
            for i in range(buttom, top-1, -1):
                matrix[i][left] = cur
                cur += 1
            left += 1
        return matrix