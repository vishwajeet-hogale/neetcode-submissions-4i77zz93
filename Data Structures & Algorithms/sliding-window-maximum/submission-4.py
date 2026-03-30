import heapq
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        st = 0
        for end, num in enumerate(nums):

            # remove smaller elements from the back
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(end)

            # shrink window
            if (end - st + 1) > k:
                st += 1
            # remove elements outside window
            if dq[0] < st:
                dq.popleft()


            # record result
            if (end - st + 1) == k:
                result.append(nums[dq[0]])

        return result

            