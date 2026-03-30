class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        memo = dict()
        def recurse1(i):
            if i >= n - 1:
                return 0
            if i in memo:
                return memo[i]
            choice1 = nums[i] + recurse1(i+2)
            choice2 = recurse1(i+1)

            memo[i] = max(choice1, choice2)
            return memo[i]

        def recurse2(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            choice1 = nums[i] + recurse2(i+2)
            choice2 = recurse2(i+1)

            memo[i] = max(choice1, choice2)
            return memo[i]
        val1 = recurse1(0)
        memo = dict()
        val2 = recurse2(1)
        return max(val1, val2)


            