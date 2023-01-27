#DP

def solution(alp, cop, problems):
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    max_alp = max(problems,key = lambda x:x[0])[0]
    max_cop = max(problems,key = lambda x:x[1])[1]
    d = [set() for i in range(150)] # d[x] x시간 후 존재할수있는 (alp,cop)쌍
    d[0].add((alp,cop))
    for i in range(150):

        min_alp=-1
        min_cop=-1
        for cur_alp,cur_cop in d[i].copy(): #(15,20)과 (20,20)이 함께있으면 (15,20)은 하위호환이니 삭제,copy사용해서 for중 삭제해도 문제 없게함
            if cur_alp > min_alp and cur_cop > min_cop:
                min_alp,min_cop = cur_alp,cur_cop
            elif cur_alp <= min_alp and cur_cop <= min_cop:
                d[i].remove((cur_alp,cur_cop))

        for cur_alp,cur_cop in d[i]:
            if cur_alp >= max_alp and cur_cop >= max_cop:
                return i
            for prob in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = prob[0],prob[1],prob[2],prob[3],prob[4]
                if alp_req <= cur_alp and cop_req <= cur_cop and i+cost<150:
                    d[i+cost].add((cur_alp+alp_rwd,cur_cop+cop_rwd))
            




print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))

# binary search + heap
# 정확성 통과, 효율성X

# 최단시간??
# 현재 할수있는 행동중 가장 적은비용으로 알고,코드를 올릴 수있는 행동 하면 되나?
# 제일 가까운 문제부터 정복하는것이 맞나? X
# 알고 5를 올려 정복할수있는 문제가 point를 코딩 0 주는데 코딩 6을 올려 정복할수있는 문제가 알고를 5씩 주면 후자부터 하는게 나음
# 답에 근접한 것부터 보고싶은데 cost가 낮다고 무조건 답에 근접한건x
# 특정 시간 미만으로 가면 아예 불가, 이상이면 가능 >> parametric search??

# from heapq import heappop, heappush
# def solution(alp, cop, problems):
#     def solve(limit):
#         # q = deque([])
#         q = []
#         # q.append((alp,cop,0))
#         heappush(q,(-alp-cop,-alp,-cop,0))

#         while q:
#             # cur_alp,cur_cop,cur_cost = q.popleft()
#             _,cur_alp,cur_cop,cur_cost = heappop(q)
#             cur_alp *= -1
#             cur_cop *= -1
#             if cur_alp >= max_alp and cur_cop >= max_cop:
#                 return True
#             for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
#                 if alp_req <= cur_alp and cop_req <= cur_cop and cur_cost+cost <= limit:
#                     q.append((-cur_alp-alp_rwd-cur_cop-cop_rwd,-cur_alp-alp_rwd,-cur_cop-cop_rwd,cur_cost+cost))
#             if cur_cost < limit:
#                 q.append((-cur_alp-cur_cop-1,-cur_alp-1,-cur_cop,cur_cost+1))
#                 q.append((-cur_alp-cur_cop-1,-cur_alp,-cur_cop-1,cur_cost+1))
#         return False
    
#     st=0
#     en=150
#     max_alp = max(problems,key = lambda x:x[0])[0]
#     max_cop = max(problems,key = lambda x:x[1])[1]
#     while st<en:
#         mid = (st+en)//2
#         if solve(mid):
#             en = mid
#         else:
#             st = mid+1
#     return st