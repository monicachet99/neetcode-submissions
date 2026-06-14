class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
            low = 1
            high = max(p)

            while low < high:
                s = (low + high) // 2

                k = 0
                for x in range(len(p)):
                    k += (p[x] + s - 1) // s

                if k <= h:
                    high = s   # try smaller speed
                else:
                    low = s + 1  # need bigger speed

            return low
                