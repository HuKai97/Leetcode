'''
输入：邻接矩阵，
输出，源点V0到各点的最小距离
'''
def Dijkstra(graph,v0):
    n=len(graph)
    # final保存那些已经被选定的点，D保存当前已经被选定点的最小路径，
    final,D=[0]*n,[0]*n
    for i in range(n):
        D[i]=graph[v0][i]
    D[v0] = 0
    final[v0] = 1
    for v in range(1,n):
        min = float("Inf")
        for w in range(0,n): # 实现最小优先队列的效果
            if not final[w] and D[w]<min: # 还没有被选定而且当前距离最小
                k=w
                min = D[w]
        final[k]=1 # 选定的点被加入到已经被选择的集合
        for w in range(0,n):
            # 还没有被选定而且距离比原先小
            if not final[w] and min + graph[k][w]<D[w]:
                D[w]=min + graph[k][w]
        print(D)
    return D


graph=[]
for i in range(0,5):
    distance=input().replace("-1","99999")
    x=list(map(int,distance.split()))
    graph.append(x)
print("初始情况：")
for m in graph:
    print(m)
print(Dijkstra(graph,0))

