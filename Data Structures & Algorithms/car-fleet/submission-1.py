class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = {}

        for i in range(len(position)):
            l[position[i]] = speed[i]

        sorted_d = dict(sorted(l.items(), reverse=True))

        d = []

        for key, value in sorted_d.items():
            t = (target - key) / value
            d.append(t)

        fleets = 0
        prev_time = 0

        for time in d:
            if time > prev_time:
                fleets += 1
                prev_time = time

        return fleets