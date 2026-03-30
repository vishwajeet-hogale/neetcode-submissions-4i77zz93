class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # if n <= 2:
        #     return max(nums)
        # dp = [nums[0], max(nums[:2])]


        # for i in range(2, n):
        #     dp.append(max(dp[i-2] + nums[i], dp[i-1]))

        # return max(dp[n-1], dp[n-2])
        memo = dict()
        def recurse(i):
            if i >= n :
                return 0
            if i in memo:
                return memo[i]
            choice1 = nums[i] + recurse(i+2)
            choice2 = recurse(i+1)

            memo[i] = max(choice1, choice2)
            return memo[i]

        return recurse(0)