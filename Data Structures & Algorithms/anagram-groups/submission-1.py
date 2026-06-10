class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = []

        for i in range(len(strs)):
            s.append(strs[i])
            s[i] = "".join(sorted(s[i]))

        d = set()
        m = []
        used = set()   

        for i in range(len(s)):
            if i in used:
                continue

            key = s[i]
            d.add(key)

            m.append([])
            m[-1].append(strs[i])
            used.add(i)

            for j in range(i + 1, len(s)):
                if j not in used and s[j] == key:
                    m[-1].append(strs[j])
                    used.add(j)

        return m