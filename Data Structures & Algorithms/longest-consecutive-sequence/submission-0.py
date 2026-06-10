class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums.sort()

        l = []
        m = 0
        p = 0

        for i in range(0, len(nums)):

            if i == 0:
                m = 1
                p = nums[i]

            elif nums[i] == p:
                continue

            elif (nums[i] - p) == 1:
                m += 1
                p = nums[i]

            else:
                l.append(m)
                m = 1
                p = nums[i]

        l.append(m)

        return max(l)