class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        for i in range(0,len(heights)-1):
            for j in range(i+1,len(heights)):
                p=(j-i)*min(heights[i],heights[j])
                m=max(m,p)

        return m 