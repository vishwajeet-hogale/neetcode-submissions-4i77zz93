class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])
        self.matrix_sum = [[0 for _ in range(self.m)] for _ in range(self.n)]
        self.matrix_sum[0][0] = self.matrix[0][0]
        self.fill_matrix()   # moved here

    def fill_matrix(self):
        # print(self.matrix)

        for i in range(1, self.m):
            self.matrix_sum[0][i] = self.matrix_sum[0][i-1] + self.matrix[0][i]

        for i in range(1, self.n):
            self.matrix_sum[i][0] = self.matrix_sum[i-1][0] + self.matrix[i][0]

        for i in range(1, self.n):
            for j in range(1, self.m):
                self.matrix_sum[i][j] = (
                    self.matrix[i][j]
                    + self.matrix_sum[i-1][j]
                    + self.matrix_sum[i][j-1]
                    - self.matrix_sum[i-1][j-1]
                )

        # print(self.matrix_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        box4 = self.matrix_sum[row2][col2]
        box2 = self.matrix_sum[row1-1][col2] if row1 > 0 else 0
        box3 = self.matrix_sum[row2][col1-1] if col1 > 0 else 0
        box1 = self.matrix_sum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return box4 - box2 - box3 + box1