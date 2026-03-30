from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        st, end, n = 0, 0, len(nums)
        res = []

        while end < n:
            # Maintain decreasing deque
            while dq and nums[dq[-1]] < nums[end]:
                dq.pop()
            dq.append(end)

            # Shrink window if needed
            if (end - st + 1) > k:
                st += 1

            # Remove elements outside window
            if dq and dq[0] < st:
                dq.popleft()

            # Record result
            if (end - st + 1) == k:
                res.append(nums[dq[0]])

            end += 1

        return res