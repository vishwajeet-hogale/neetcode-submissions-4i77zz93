class Solution:
    def numDecodings(self, s: str) -> int:
        hash_map = dict()

        for i in range(1,27):
            hash_map[str(i)] = chr(65 + i)

        cnt = 0
        memo = dict()
        def recurse(s, tmp):
            if len(s) == 0:
                print(tmp)
                return 1
            if s in memo:
                return memo[s]
            # print(s)
            cnt = 0
            for idx in range(len(s)):
                slc = s[:idx+1]
                if slc in hash_map:
                    cnt += recurse(s[idx+1:], tmp + "," + slc)
            memo[s] = cnt
            return memo[s]

        return recurse(s, "")

            
        