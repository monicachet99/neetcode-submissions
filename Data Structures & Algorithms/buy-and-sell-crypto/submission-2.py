class Solution:
    def maxProfit(self, a: List[int]) -> int:
        
        p=0
        l=a[0]

        for i in range(0,len(a)):

            if a[i]<l:
                l=a[i]

            if a[i]-l>p:
                p=a[i]-l

        return p