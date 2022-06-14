class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        num1 = -1
        num2 = -1
        count1 = 0
        count2 = 0
        
        for elem in nums:
            if elem == num1:
                count1 += 1
            elif elem == num2:
                count2 += 1
            elif count1 == 0:
                num1 = elem
                count1 = 1
            elif count2 == 0:
                num2 = elem
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        targetCount = len(nums)//3
        count1 = 0
        count2 = 0
        ans = []
        # print(num1, num2)
        for elem in nums:
            if elem == num1:
                count1 += 1
            elif elem == num2:
                count2 += 1
                
        if count1 > targetCount:
            ans.append(num1)
        if count2 > targetCount:
            ans.append(num2)
                
        # print(count1, count2 )
        return ans
        