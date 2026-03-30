class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            "0":"+"
        }
        
        n = len(digits)
        res = []
        def dfs(i, tmp):
            if i >= n:
                res.append(tmp)
                return

            choices = hash_map[digits[i]]
            for choice in choices:
                tmp += choice
                dfs(i+1, tmp)
                tmp = tmp[:-1]

            return
        if digits == "":
            return []
        dfs(0, "")
        return res

            
            