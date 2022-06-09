class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        
        for i in range(0, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(0, n):
            matrix[i].reverse()