class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2: return n
        # dp[i]表示第i个节点为根节点的二叉搜索树共有多少个
        dp = [0 for _ in range(n+1)]
        dp[0] = 1  # 0个节点有1种二叉搜索树  []
        dp[1] = 1  # 1个节点有1种二叉搜索树  [root]
        for i in range(2, n+1):
            for j in range(1, i+1):  # 最多根节点可以等于i 右子树可以为空的
                # 左子树 1~j-1  j-1-1+1 = j - 1
                # 右子树 j+1~i  i-j-1+1 = i - j
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]