class Solution:
    def findTwoElement( self,arr, n): 
        
        sumOfElem = 0
        sumOfSquaredElem = 0
        
        targetElemSum = n * (n+1) // 2
        targetSquaredElemSum = n * (n + 1) * (2*n + 1) // 6
        
        for elem in arr:
            sumOfElem += elem
            sumOfSquaredElem += elem*elem
        
        # X = Missing Number
        # Y = Repeating Number
        
        # X - Y = tempA   
        tempA = targetElemSum - sumOfElem
        
        # X+Y = tempB
        tempB = (targetSquaredElemSum - sumOfSquaredElem) // tempA
        
        a = (tempB - tempA) // 2
        b = (tempB + tempA) // 2
        
        return a, b