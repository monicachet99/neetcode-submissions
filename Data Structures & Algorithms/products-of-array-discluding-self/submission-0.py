class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        k = 0
        n = len(nums)
        l = []

        while k < n:

            p = math.prod(nums[k+1:n]) * math.prod(nums[0:k])

            l.append(p)
            k += 1

        return l