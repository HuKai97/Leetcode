class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def dfs(n, A, B, C):
            if n == 1:
                C.append(A.pop())
                return
            else:
                dfs(n-1, A, C, B)   # 把A上面n-1个节点从A移动到B
                C.append(A.pop())   # 再把最后一个节点从A移动到C
                dfs(n-1, B, A, C)   # 再把B中的n-1个节点从B移动到C
        n = len(A)
        dfs(n, A, B, C)   # 把A中n个节点通过B移动到C