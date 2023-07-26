class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k == 0 or k == len(nums) or len(nums) == 1:
            return 
        
        k = k%len(nums)
        
        temp = []
        for i in range(len(nums)-k):
            temp.append(nums[i])
            
        j = 0
        for i in range(len(nums)-k,len(nums)):
            nums[j] = nums[i]
            j+=1
            
        j = 0
        for i in range(k,len(nums)):
            nums[i] = temp[j]
            j+=1
            
        
        
        
        