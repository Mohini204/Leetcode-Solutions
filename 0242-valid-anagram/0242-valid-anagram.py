from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        count = [0]*27
        
        for ch in range(len(s)):
            count[ord(s[ch])-ord('a')] += 1
            count[ord(t[ch])-ord('a')] -= 1
                
        for i in count:
            if i != 0:
                return False
            
        return True
                
        
  
        
        
        
        
        
        
        
        
    
            