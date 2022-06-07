class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        
        # step 1
        i = n-1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        
        downCurve = i-1
        
        if downCurve >= 0:
            # step 2
            i = n-1
            while i > 0:
                if nums[i] > nums[downCurve]:
                    break
                i -= 1
            upCurve = i

            # step 3
            nums[upCurve], nums[downCurve] = nums[downCurve], nums[upCurve]
        
        # step 4
        startPtr = downCurve + 1
        endPtr = n - 1
        
        while startPtr <= endPtr:
            nums[startPtr], nums[endPtr] = nums[endPtr], nums[startPtr]
            startPtr += 1
            endPtr -= 1