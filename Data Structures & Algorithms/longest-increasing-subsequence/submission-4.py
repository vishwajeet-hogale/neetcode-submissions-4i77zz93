class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = dict()
        def recurse(i, prev):
            if i == n:
                return 0
            if (i, prev) in memo:
                return memo[(i,prev)]
            res = 0

            # Only recurse forward when valid
            for j in range(i, n):
                if prev is None or nums[j] > prev:
                    res = max(res, 1 + recurse(j + 1, nums[j]))

            memo[(i,prev)] = res
            return memo[(i,prev)]

        return recurse(0, None)