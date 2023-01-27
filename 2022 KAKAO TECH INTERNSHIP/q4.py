# 걍 다익스트라 쓰면 될듯???
from heapq import heappush, heappop
inf = float('inf')

def solution(n, paths, gates, summits):
    exist_en = set(summits)
    exist_st = set(gates)

    adj = {i:[] for i in range(1,n+1)}
    for a,b,cost in paths:
        adj[a].append((b,cost))
        adj[b].append((a,cost))
    ans = [0,inf]
    q = []
    dis = [inf]*(n+1)

    for st in gates:
        dis[st] = 0
        heappush(q,(0,st))

    while q:
        cur_dis,cur = heappop(q)
        if cur_dis > dis[cur]: continue
        for dir,cost in adj[cur]:
            cost = max(dis[cur],cost)
            if dir not in exist_st and dis[dir] > cost:
                dis[dir] = cost
                if dir not in exist_en:
                    heappush(q,(dis[dir],dir))
    for en in sorted(summits):
        if dis[en] < ans[1]:
            ans[1] = dis[en]
            ans[0] = en
    
    return ans
# print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
# [3, 7],
# [1, 5]))
print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
[1, 3],
[5]))