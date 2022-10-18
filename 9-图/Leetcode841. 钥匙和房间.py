# bfs
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        used = [False for _ in range(len(rooms))]
        used[0] = True
        while queue:
            cur = queue.pop(0)
            next_nodes = rooms[cur]
            for next_node in next_nodes:
                if used[next_node] == False:
                    used[next_node] = True
                    queue.append(next_node)
        for falg in used:
            if falg == False: return False
        return True


# dfs
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(idx, used):
            if used[idx] == True: return
            used[idx] = True
            next_nodes = rooms[idx]
            for next_node in next_nodes:
                dfs(next_node, used)

        used = [False for _ in range(len(rooms))]
        dfs(0, used)
        for i in range(len(used)):
            if used[i] == False: return False
        return True