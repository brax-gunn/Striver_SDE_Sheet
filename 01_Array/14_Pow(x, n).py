class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        isNegative = False
        if n < 0:
            isNegative = True
            
        ans = 1     
        n = abs(n)
        
        while n > 0:
            if n%2 == 0:
                x = x * x
                n = n//2
            else:
                ans = ans * x
                n -= 1
        
        if isNegative:
            return 1 / ans
        else:
            return ans
                