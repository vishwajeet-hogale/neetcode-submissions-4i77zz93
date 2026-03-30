class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        while k:
            k -= 1
            last = nums[-1]
            prev = nums[0]
            for i in range(1,n):
                temp = nums[i]
                nums[i] = prev
                prev = temp
            nums[0] = last

        return nums

        