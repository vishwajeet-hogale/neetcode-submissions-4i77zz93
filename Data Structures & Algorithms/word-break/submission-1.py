class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def check(tmp):
            for word in set(tmp):
                if word not in wordDict:
                    return False
            return True
        def dfs(i, tmp):
            if i >= n:
                return check(tmp)
            if i in memo:
                return memo[i]

            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    tmp += [s[i:j+1]]
                    if dfs(j+1, tmp):
                        memo[i] = True
                        return True
                    tmp = tmp[:-1]

            memo[i] = False
            return False

        return dfs(0, [])
