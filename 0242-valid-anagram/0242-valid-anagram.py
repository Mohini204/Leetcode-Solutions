from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0]*27
        
        for ch in s:
            count[ord(ch)-ord('a')] += 1
            
        for ch in t:
            if count[ord(ch)-ord('a')] == 0:
                return False
            else:
                count[ord(ch)-ord('a')] -= 1
                
        for i in count:
            if i != 0:
                return False
            
        return True
                
        
  
        
        
        
        
        
        
        
        
    
            