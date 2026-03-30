class Solution:
    def numDecodings(self, s: str) -> int:
        hash_map = dict()

        for i in range(1,27):
            hash_map[str(i)] = chr(65 + i)
        # print(hash_map)
        cnt = 0
        memo = dict()
        def recurse(s):
            if len(s) == 0:
                return 1
            if s in memo:
                return memo[s]
            cnt = 0
            for idx in range(len(s)):
                slc = s[:idx+1]
                if slc in hash_map:
                    cnt += recurse(s[idx+1:])
            memo[s] = cnt
            return memo[s]

        return recurse(s)

            
        