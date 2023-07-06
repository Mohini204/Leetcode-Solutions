class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) == 1:
            return
        
        while k>len(nums):
            k = k-len(nums)
            
        if k == len(nums):
            return
        
        rev = []
        
        for i in range(0,len(nums)-k):
            rev.append(nums[i])
        
        i = len(nums)-k
        j = 0
        
        while i < len(nums):
            nums[j] = nums[i]
            i+=1
            j+=1
            
        j=0
        
        
        for i in range(k,len(nums)):
            nums[i] = rev[j]
            j+=1
            
        
        
        