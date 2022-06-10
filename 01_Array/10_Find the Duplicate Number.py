class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPointer = nums[0]
        fastPointer = nums[0]
        
        while True:
            slowPointer = nums[slowPointer]
            fastPointer = nums[fastPointer]
            fastPointer = nums[fastPointer]
            
            if slowPointer == fastPointer:
                break
            
        fastPointer = nums[0]
        while slowPointer != fastPointer:
            slowPointer = nums[slowPointer]
            fastPointer = nums[fastPointer]
        
        return slowPointer