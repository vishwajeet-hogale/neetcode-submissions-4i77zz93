from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.pntCounts = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts.append(tuple(point))
        self.pntCounts[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x,y in self.pts:
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += self.pntCounts[(x,py)] * self.pntCounts[(px, y)]

        return res
        
