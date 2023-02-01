


def solution(info, edges):
    n = len(info)
    adj = {i:[] for i in range(n)}
    vis = {}
    for st,en in edges:
        adj[st].append(en)
    ans = [0]

    def dfs(state):
        if vis.get(state,False): return None
        vis[state] = True
        wolf,num = 0,0
        for cur in range(n):
            if state & (1<<cur):
                num+=1
                wolf += info[cur]
        if wolf >= num/2: return None
        ans[0] = max(ans[0],num-wolf)

        for cur in range(n):
            if not state & (1<<cur):
                continue
            for dir in adj[cur]:
                dfs(state | (1<<dir))

    dfs(1)
    return ans[0]


print(solution(	[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))