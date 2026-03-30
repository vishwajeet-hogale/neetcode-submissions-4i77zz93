class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        seen = set()
        for i in nums:
            seen.add(i)
        max_len = 1
        for num in nums:
            if (num - 1) not in seen:
                parent = int(num)
                num += 1
                while num in seen:
                    max_len = max(max_len, num - parent + 1)
                    num += 1

        return max_len

