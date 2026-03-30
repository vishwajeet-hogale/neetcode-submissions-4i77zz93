class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        memo = dict()
        def recurse(i, target):
            if i == 0:
                return 0
            if target == 0:
                return 1
            if (i, target) in memo:
                return memo[(i,target)]
            if coins[i-1] <= target:
                memo[(i, target)] = recurse(i, target - coins[i-1]) + recurse(i-1, target)
            else:
                memo[(i,target)] = recurse(i-1, target)
            return memo[(i,target)]

        return recurse(n, amount)