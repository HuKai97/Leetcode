class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    if j not in edges[i]: edges[i].append(j)
                    if i not in edges[j]: edges[j].append(i)
        count = 0
        used = [False for _ in range(n)]
        for node in range(n):
            if used[node] == False:
                used[node] = True
                queue = [node]
                while queue:
                    cur_node = queue.pop(0)
                    for next_node in edges[cur_node]:
                        if used[next_node] == False:
                            used[next_node] = True
                            queue.append(next_node)
                count += 1
        return count


# dfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(idx, used, edges):
            if used[idx] == True: return
            used[idx] = True
            next_nodes = edges[idx]
            for next_node in next_nodes:
                dfs(next_node, used, edges)


        n = len(isConnected)
        edges = [[]for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    if j not in edges[i]: edges[i].append(j)
                    if i not in edges[j]: edges[j].append(i)
        count = 0
        queue = []
        used = [False for _ in range(n)]
        for i in range(n):
            if used[i] == False:
                dfs(i, used, edges)
                count += 1
        return count