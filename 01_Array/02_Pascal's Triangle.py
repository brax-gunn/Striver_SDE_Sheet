class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []
        currentRow = 1
        while currentRow <= numRows:
            pascalTriangle.append(self.__getPascalRow(currentRow))
            currentRow += 1
        return pascalTriangle
    
    def __getPascalRow(self, rowNumber):
        row = rowNumber
        col = 0
        
        countOfElem = 1
        temp = [1]
        prevAns = 1
        while countOfElem < rowNumber:
            prevAns = (prevAns * (row-1))//(col+1)
            temp.append( prevAns  )
            row -= 1
            col += 1
            countOfElem += 1
        
        return temp