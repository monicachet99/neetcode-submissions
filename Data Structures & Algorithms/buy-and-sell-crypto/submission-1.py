class Solution:
    def maxProfit(self, a: List[int]) -> int:
        
        h=0
        l=a[0]

        for i in range(0,len(a)):

            if a[i]<l:
                l=a[i]

            if a[i]-l>h:
                h=a[i]-l

        return h