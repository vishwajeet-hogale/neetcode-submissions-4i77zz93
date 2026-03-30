from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = dict(Counter(s1))
        window_size = len(s1)
        st, n, end = 0, len(s2) , 0
        s2_dict = dict()
        while end < n :
            s2_dict[s2[end]] = s2_dict.get(s2[end], 0) + 1
            print(s2_dict)
            while (end - st + 1) > window_size:
                s2_dict[s2[st]] -=1
                if s2_dict[s2[st]] == 0:
                    del s2_dict[s2[st]]
                st += 1
            if s1_dict == s2_dict:
                return True

            end += 1
        return False