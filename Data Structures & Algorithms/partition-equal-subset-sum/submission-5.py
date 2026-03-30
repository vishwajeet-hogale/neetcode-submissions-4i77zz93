class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0
        for i in nums:
            total_sum += i
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2

        n = len(nums)
        memo = dict()
        def subset_sum(i, target):
            if i == 0:
                if target == 0:
                    # print(tmp)
                    memo[(i, target)] = True
                else:
                    memo[(i, target)] = False
                return memo[(i, target)]

            if (i, target) in memo:
                return memo[(i, target)]
            choice1, cjoice2 = False, False
            if nums[i-1] <= target:
                choice1 = subset_sum(i-1, target - nums[i-1])
            choice2 = subset_sum(i-1, target)
            
            memo[(i,target)] = choice1 or choice2
            return memo[(i, target)]
        
        return subset_sum(n, target_sum)
        


        