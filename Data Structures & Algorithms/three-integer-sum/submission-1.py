class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            target = -nums[i]

            while l < r:

                total = nums[l] + nums[r]

                if total == target:

                    triplet = (nums[i], nums[l], nums[r])
                    res.add(triplet)

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < target:
                    l += 1

                else:
                    r -= 1

        return [list(x) for x in res]