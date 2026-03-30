import math
class Solution:
    def check(self, rate, piles, h):
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile / rate)

        return hrs <= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            if self.check(mid, piles, h):
                r = mid

            else:
                l = mid + 1
        return l

        