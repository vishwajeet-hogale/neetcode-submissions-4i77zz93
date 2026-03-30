from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque()
        merged = [(pos, score) for pos, score in zip(position, speed)]
        merged = sorted(merged, key = lambda x : x[0])
        print(merged)
        # stack = [marged[-1]]
        n = len(merged)
        for i in range(n-1, -1, -1):
            pos, speed = merged[i]
            time_to_reach = (target - pos) / speed
            if not stack:
                stack.append(time_to_reach)
                continue 
            if time_to_reach > stack[-1]:
                stack.append(time_to_reach)
            
        return len(stack)
