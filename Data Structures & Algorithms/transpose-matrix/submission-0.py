class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        if n == m:
            for i in range(n):
                for j in range(i+1):
                    temp = int(matrix[i][j])
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

            return matrix

        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = matrix[j][i]

        return res