class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        i, j = 0, n - 1
        vis = set()
        res = []
        for i in range(n):
            for j in range(n-1, i+2, -1):
                p, q = i + 1, j - 1
                while p < q:
                    s = nums[i] + nums[j] + nums[p] + nums[q]
                    if (nums[i],nums[p],nums[q], nums[j]) in res:
                        p += 1
                        q -= 1
                        continue
                    if s == target:
                        vis.add((nums[i],nums[p],nums[q], nums[j]))
                        res.append((nums[i],nums[p],nums[q], nums[j]))
                        p += 1
                        q -= 1
                        
                    elif s < target:
                        p += 1
                    else:
                        q -= 1

        return list(res)

        