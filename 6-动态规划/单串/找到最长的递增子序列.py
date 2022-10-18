def solver(a, n):
    if n < 2:
        print(n)
    # dp[i]表示以a[i]结尾的数组的最长递增子序列
    max_len = 1
    dp = [1 for _ in range(n)]
    pre_pos = [i for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    pre_pos[i] = j
        if max_len < dp[i]: max_len = dp[i]

    for i in range(n):
        if dp[i] == max_len:
            idx = i
            break

    res = []
    while idx >= 0:
        if len(res) == max_len: break
        res.append(str(a[idx]))
        idx = pre_pos[idx]

    print(' '.join(res[::-1]))


T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    solver(a, n)