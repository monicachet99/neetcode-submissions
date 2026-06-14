class Solution:
    def findMedianSortedArrays(self, l1: List[int], l2: List[int]) -> float:
        l=l1+l2
        l.sort()
        n = len(l)

  
        if n % 2 == 1:
            return l[n // 2]
        else:
            return (l[n // 2 - 1] + l[n // 2]) / 2