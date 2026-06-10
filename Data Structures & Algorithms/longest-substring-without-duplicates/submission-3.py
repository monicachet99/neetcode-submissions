class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=0
        d=""
        l=[]
        if s=="":
            return 0

        for i in s:

            if i not in d:
                n+=1
                d+=i

            else:

                while i in d:
                    d=d[1:]

                d+=i
                n=len(d)

            l.append(n)

        return max(l)