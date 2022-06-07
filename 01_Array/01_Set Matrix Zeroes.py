class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        columns = []
        
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.append(row)
                    columns.append(col)
                    
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if row in rows or col in columns:
                    matrix[row][col] = 0