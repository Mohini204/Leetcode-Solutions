class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            return 1
        
        
        n = len(citations)
        best = 0
        bestIdx = 0
        
        for i in range(n):
            
            if (n-i) <= citations[i] and (n-i)>bestIdx:
                best = citations[i]
                bestIdx = n-i
                
        return bestIdx
                
        