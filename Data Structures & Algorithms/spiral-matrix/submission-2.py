class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        col_st, col_end = 0, m-1
        row_st, row_end = 0, n-1
        res = []
        while row_st <= row_end and col_st <= col_end:
            # Go right
            for y in range(col_st, col_end + 1):
                res.append(matrix[row_st][y])
            row_st += 1
            
            # Go down
            for x in range(row_st, row_end + 1):
                res.append(matrix[x][col_end])
            col_end -= 1
            
            # Go left
            if row_st <= row_end:
                for y in range(col_end, col_st - 1, -1):
                    res.append(matrix[row_end][y])
                row_end -= 1
            
            # Go up
            if col_st <= col_end:
                for x in range(row_end, row_st - 1, -1):
                    res.append(matrix[x][col_st])
                col_st += 1

        return res

        
        
        
        