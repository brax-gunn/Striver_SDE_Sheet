Pascal Triangle

To get elem of Pascal Triangle formula is: $^{row-1}C_{col-1}$

To generate any row of Pascal Triangle...

```python
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
```

