class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        
        if len(nums) == 1: return 1
        
        c,i = 1,1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                c+=1
                if c > 2:
                    nums.pop(i)
                    i-=1
                i+=1
            else:
                i+=1
                c=1
            
        return len(nums)
        