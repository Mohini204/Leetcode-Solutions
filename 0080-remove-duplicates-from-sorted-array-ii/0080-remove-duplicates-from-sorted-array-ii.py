class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        
        if len(nums) == 1: return 1
        
        c,i, j = 1,1,1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                c+=1
                if c <= 2:
                    nums[j] = nums[i]
                    i+=1
                    j+=1
                else:
                    i+=1
                    
            else:
                c = 1
                nums[j] = nums[i]
                i+=1
                j+=1
                
        return j
        