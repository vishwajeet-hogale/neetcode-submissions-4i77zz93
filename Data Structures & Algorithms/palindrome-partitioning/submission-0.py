class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def valid(s1):
            return s1 == s1[::-1]
        def dfs(s1, temp):
            if not s1:
                res.append(temp)
                return 

            for i in range(len(s1)):
                slice_s = s1[:i+1]
                if valid(slice_s):
                    dfs(s1[i+1:], temp + [slice_s])


        dfs(s, [])
        return res
                
