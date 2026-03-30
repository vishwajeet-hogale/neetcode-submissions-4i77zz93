class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for i in range(len(nums)):
            if maxJump < i:
                return False
            maxJump = max(i + nums[i], maxJump)

        return True
        