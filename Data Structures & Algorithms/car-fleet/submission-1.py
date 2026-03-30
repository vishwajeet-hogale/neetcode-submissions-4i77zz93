class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p,s) for p, s in zip(position, speed)]
        arr = sorted(arr, key = lambda x: x[0])
        n = len(arr)
        stack = []
        for i in range(n-1, -1, -1):
            stack.append((target - arr[i][0])/ arr[i][1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        print(stack)
        return len(stack)