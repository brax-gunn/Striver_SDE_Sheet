class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return []
        
        intervals.sort()
        
        mergedIntervals = []
        
        refPair = intervals[0]
        
        for currentPair in intervals:
            if currentPair[0] <= refPair[1]:
                refPair[1] = max(currentPair[1], refPair[1])
            else:
                mergedIntervals.append(refPair)
                refPair = currentPair
        
        mergedIntervals.append(refPair)
        
        return mergedIntervals

        