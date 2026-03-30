from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()

        for char in tokens:

            if char in ["*", "+", "-", "/"]:
                if len(dq) >= 2:
                    val1 = dq.pop()
                    val2 = dq.pop()
                    res = None
                    if char == "*":
                        res = val1 * val2
                        dq.append(res)
                    elif char == "+":
                        res = val1 + val2
                        dq.append(res)
                    elif char == "-":
                        res = val2 - val1
                        dq.append(res)
                    else:
                        res = int(val2 / val1)
                        dq.append(res)

                continue

            dq.append(int(char))

        return dq[0]


                    
        