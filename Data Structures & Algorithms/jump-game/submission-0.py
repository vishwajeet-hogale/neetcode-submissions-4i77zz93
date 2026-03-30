class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for i, jump in enumerate(nums):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + jump)
        
        return True
        