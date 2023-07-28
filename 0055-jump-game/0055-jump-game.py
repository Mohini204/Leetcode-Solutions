class Solution:
    
    def canJumpHelper(self, nums, idx, ans):
        
        if ans[idx] != 0:
            return ans[idx]
        
        
        if idx >= len(nums):
            ans[idx] = False
            return ans[idx]
        
        for i in range(idx+1,idx+nums[idx]+1):
            
            ans[i] = self.canJumpHelper(nums, i , ans)
                
            if ans[i]:
                ans[idx] = True
                return True
            
            
        ans[idx] = False
        
        return ans[0]

    
    def canJump(self, nums: List[int]) -> bool:
        
        ans = [0]*(len(nums)+1)
        ans[len(nums)-1] = True
        
        for idx in range(len(nums)-2,-1,-1):
            maxidx = min(len(nums)-1,idx+nums[idx])
            for i in range(idx+1,maxidx+1):
                if ans[i] == True:
                    ans[idx] = True
                    break
        
        return ans[0]
        
    
        
        
        