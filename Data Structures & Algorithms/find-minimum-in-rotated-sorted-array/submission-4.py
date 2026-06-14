class Solution:
    def findMin(self, n: List[int]) -> int:
        l=n[0]
        r=1
        if len(n)==1:
            return n[0]
        while l<n[r] and r<len(n)-1:
            r+=1

        if r==len(n)-1 :
            return min(l,n[r])
        else:
            return n[r]

        

        