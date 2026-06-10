class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
   
        p=0
        for i in range(0,len(nums)-1):
            
                
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]>0:
                    p=max(p,nums[j]-nums[i])


        return p