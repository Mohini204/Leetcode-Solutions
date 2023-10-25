class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        i = 0
        count = 1
        
        while i < n-1:
            
            if nums[i]+i >= n-1:
                return count
            
            elif nums[i] > 0 and (nums[i] + i) < n-1:
                j = 1
                nextbest = 0
                nextidx = 0
                while j <= nums[i]:
                    if nums[i+j] + i + j > nextbest:
                        nextbest = nums[i+j] + i + j
                        nextidx = i+j
                    j+=1
                i = nextidx
                count+=1
                
        return count
                
        