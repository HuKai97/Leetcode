class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegress = [0 for _ in range(numCourses)]  # 入度表
        edges = [[] for _ in range(numCourses)]     # 临接矩阵
        res = []
        for node1, node2 in prerequisites:   # node2 -> node1
            indegress[node1] += 1
            edges[node2].append(node1)
        queue = []
        for i in range(numCourses):
            if indegress[i] == 0: queue.append(i)
        while queue:
            pop_node = queue.pop(0)
            res.append(pop_node)
            next_nodes = edges[pop_node]
            for next_node in next_nodes:
                indegress[next_node] -= 1
                if indegress[next_node] == 0:
                    queue.append(next_node)
        if numCourses != len(res): res = []
        return res