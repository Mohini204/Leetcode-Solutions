class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        hmap = {}
        
        for i in nums:
            hmap[i] = hmap.get(i,0) + 1
            
        for key in hmap:
            if hmap[key]>len(nums)//2:
                return key
        
        
        
        
        