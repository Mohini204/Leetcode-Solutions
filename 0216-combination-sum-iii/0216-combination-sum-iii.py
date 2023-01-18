class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []

        def backtrack(n, si, sans):

            if len(sans) == k:
                if n == 0:
                    ans.append(list(sans))
                return
            
            for i in range(si,10):
                sans.append(i)
                backtrack(n-i,i+1,sans)
                sans.pop()

        
        backtrack(n, 1, [])

        return ans