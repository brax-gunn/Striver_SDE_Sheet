class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if len(matrix) == 0:
            return False
        
        N = len(matrix)
        M = len(matrix[0])
        
        return self.binarySearch(matrix, M, 0, M*N-1, target)
    
    def binarySearch(self, matrix, M, left, right, x):
        
        while left <= right:
            
            mid = left + (right - left) // 2


            if matrix[mid//M][mid%M] == x:
                return True
            elif matrix[mid//M][mid%M] < x:
                left = mid + 1
            elif matrix[mid//M][mid%M] > x:
                right = mid - 1
        
        return False