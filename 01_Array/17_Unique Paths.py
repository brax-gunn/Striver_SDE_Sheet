class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.__calcTotalPath(m, n)
    
    def __calcTotalPath(self, m, n):
        
        lookUp = [ [0 for i in range(n)] for j in range(m) ]
        
        lookUp[m-1][n-1] = 0
        
        for i in range(0, m):
            lookUp[i][n-1] = 1
            
        for j in range(0, n):
            lookUp[m-1][j] = 1
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                lookUp[i][j] = lookUp[i][j+1] + lookUp[i+1][j]
        
        return lookUp[0][0]
    