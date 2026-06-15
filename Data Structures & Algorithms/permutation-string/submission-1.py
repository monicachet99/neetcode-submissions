class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l1 = sorted(s1)
        n = len(s1)

        for i in range(len(s2) - n + 1):
            if sorted(s2[i:i+n]) == l1:
                return True

        return False