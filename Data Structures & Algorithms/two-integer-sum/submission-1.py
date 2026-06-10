class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=[]
        for i in range(0,len(nums)):
            t=target-nums[i]
            if t in nums and nums.index(t)!=i:
                d.append(i)
                d.append(nums.index(t))
                d.sort()
                return d
            
            else:
                for j in range(0,len(nums)):
                    if j==i:
                        continue
                    elif nums[j]==t:
                        d.append(i)
                        d.append(j)
                        d.sort()
                        return d


        