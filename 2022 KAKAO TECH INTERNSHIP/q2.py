from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    n = len(q1)+len(q2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    if sum1==sum2: return 0
    for i in range(2*n):
        if sum1==sum2: return i
        if sum1 > sum2:
            pop =  q1.popleft()
            q2.append(pop)
            sum1-=pop
            sum2+=pop
        elif sum2 > sum1:
            pop = q2.popleft()
            q1.append(pop)
            sum1+=pop
            sum2-=pop
    return -1

print(solution([1],[0]))
# print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
# print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
# print(solution([1, 1],[1, 5]))