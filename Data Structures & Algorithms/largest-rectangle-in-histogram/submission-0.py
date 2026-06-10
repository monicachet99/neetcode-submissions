class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0

        for i in range(len(heights)):
            k = 1

            
            r = i + 1
            while r < len(heights) and heights[r] >= heights[i]:
                k += 1
                r += 1

           
            l = i - 1
            while l >= 0 and heights[l] >= heights[i]:
                k += 1
                l -= 1

            m = max(m, heights[i] * k)

        return m