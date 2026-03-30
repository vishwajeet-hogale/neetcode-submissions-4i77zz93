from collections import defaultdict
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx, ty, tz = target
        txmap = defaultdict(int)
        tymap = defaultdict(int)
        tzmap = defaultdict(int)

        def filter_trips(x):
            if x[0] > tx or x[1] > ty or x[2] > tz:
                return False
            if x[0] > tx or x[1] > ty or x[2] > tz:
                return False
            if x[0] > tx or x[1] > ty or x[2] > tz:
                return False
            return True

        options = []
        for i in triplets:
            if filter_trips(i):
                options.append(i)
                txmap[i[0]] += 1
                tymap[i[1]] += 1
                tzmap[i[2]] += 1

        
        return True if tx in txmap and ty in tymap and tz in tzmap else False


        