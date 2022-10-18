class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # https://www.bilibili.com/video/BV1Xp4y1Y7FJ?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        # 入度：有哪些顶点指向这个顶点
        indegree = [0 for _ in range(numCourses)]  # 入度表
        edges = [[] for _ in range(numCourses)]    # 临接矩阵
        # node2 -> node1
        for node1, node2 in prerequisites:
            indegree[node1] += 1
            edges[node2].append(node1)
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            pop_node = queue.pop(0)
            numCourses -= 1
            next_nodes = edges[pop_node]
            for next_node in next_nodes:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        return numCourses == 0
