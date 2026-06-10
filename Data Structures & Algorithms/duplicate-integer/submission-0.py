class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=[]
        for i in range(0,len(nums)):
            if nums[i] in d :
                return True
            else:
                d.append(nums[i])
        return False


