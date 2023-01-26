from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def defVal():
            return 'None'
        
        d = defaultdict(defVal)
        
        for ch in s:
            d[ch] = d.get(ch,0) + 1
            
        for ch in t:
            if d[ch] == 'None':
                return False
            else:
                d[ch] -= 1
            
        for ch in d:
            if d[ch] != 0:
                return False
            
        return True
            