class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = dict()
        def recurse(i, bought):
            if i >= n :
                return 0
            if (i, bought) in memo:
                return memo[(i,bought)]
                
            res = 0
            if bought:
                res = max(res, prices[i] + recurse(i+1, False))
            else:
                res = max(res, -prices[i] + recurse(i+1, True))
            memo[(i,bought)] = max(res, recurse(i+1, bought))
            return memo[(i,bought)]

        return recurse(0, False)
            

        