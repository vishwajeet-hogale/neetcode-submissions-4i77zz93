class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [nums[0], max(nums[:2])]
        

        for i in range(2, n):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))

        return max(dp[n-1], dp[n-2])
        