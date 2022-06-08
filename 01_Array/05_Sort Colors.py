class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        lowPointer = 0
        midPointer = 0
        highPointer = len(nums)-1
        
        while midPointer <= highPointer:
            if nums[midPointer] == 0:
                nums[lowPointer], nums[midPointer] = nums[midPointer], nums[lowPointer]
                lowPointer += 1
                midPointer += 1
            
            elif nums[midPointer] == 1:
                midPointer += 1
                
            elif nums[midPointer] == 2:
                nums[midPointer], nums[highPointer] = nums[highPointer], nums[midPointer]
                highPointer -= 1
                