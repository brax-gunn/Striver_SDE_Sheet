class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):

        tempArr = [0 for _ in range(n)]
        countInv = self.mergeSort(arr, tempArr, 0, n-1)
        
        return countInv
    
    def mergeArr(self, arr, tempArr, left, mid, right):
        i,j,k,countInv = 0,0,0,0
        i = left
        j = mid
        k = left
    
        while i <= mid-1 and j <= right:
            if arr[i] <= arr[j]:
                tempArr[k] = arr[i]
                k+=1
                i+=1
            else:
                tempArr[k] = arr[j]
                k+=1
                j+=1
                countInv += (mid-i)
        
        while i <= mid-1:
            tempArr[k] = arr[i]
            k += 1
            i += 1
        
        while j <= right:
            tempArr[k] = arr[j]
            k += 1
            j += 1
        for m in range(left, right+1):
            arr[m] = tempArr[m]
    
        return countInv
    
    
    def mergeSort(self, arr, tempArr, left, right):
        countInv = 0
    
        if left < right:
            mid = ( left + right ) // 2
    
            countInv += self.mergeSort(arr, tempArr, left, mid)
            countInv += self.mergeSort(arr, tempArr, mid+1, right)
            countInv += self.mergeArr(arr, tempArr, left, mid+1, right)
    
        return countInv

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends