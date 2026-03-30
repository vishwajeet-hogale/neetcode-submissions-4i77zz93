from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        ad_list = defaultdict(list)
        for i,j in prerequisites:
            ad_list[j].append(i)
            inDegree[i] += 1

        start_nodes = [i for i, val in enumerate(inDegree) if val == 0]
        vis = set()
        for st in start_nodes:
            queue = deque()
            queue.append(st)

            while len(queue):
                curr_node = queue.popleft()
                vis.add(curr_node)
                for neig in ad_list[curr_node]:
                    if neig not in vis:
                        inDegree[neig] -= 1
                        if inDegree[neig] == 0:
                            queue.append(neig)
                    else:
                        return False
        return len(vis) == numCourses

                
        