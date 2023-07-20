class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        
        i, j = 0,0
        idx = -1
        
        for i in range(len(haystack)):
            
            k = i
            while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                if j == 0:
                    idx = k
                if j == len(needle) - 1:
                    return idx
                k+=1
                j+=1
                
            j = 0
            idx = -1
            
        return idx
                
        