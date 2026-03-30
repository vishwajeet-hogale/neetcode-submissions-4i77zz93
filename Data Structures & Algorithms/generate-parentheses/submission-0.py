class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def validate(string):
            stack = []
            mapd = {
                ")" : "(",
            }
            for i in string:
                if i == "(":
                    stack.append(i)
                elif len(stack) and i == ")":
                    if stack[-1] == mapd[i]:
                        stack = stack[:-1]
                    else:
                        return False
                # else:
                #     return False
            return len(stack) == 0


        def helper(l,r, temp):
            if l < 0 or r < 0:
                return
            if l == 0 and r == 0:
                if validate(temp):
                    res.append(temp)
                return

            helper(l-1,r, temp + "(")
            helper(l, r-1, temp + ")")

        helper(n, n, "")
        return res