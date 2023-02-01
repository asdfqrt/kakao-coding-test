import math
from collections import defaultdict
def solution(fees, records):
    mt,mp,tl,pl =  fees
    dic = {}
    ans = defaultdict(int)
    for string in records:
        time,car,inout = string.split()
        hour,minute = time.split(":")
        cur = int(hour) * 60 + int(minute)
        if car not in dic:
            dic[car] = cur
        else:
            ans[car] += cur - dic[car]
            del dic[car]
    for car in dic:
        ans[car] += (1439-dic[car])
    for car in ans:
        if ans[car] > mt:
            ans[car] = mp + (math.ceil((ans[car]-mt)/tl) *pl)
        else:
            ans[car] = mp
    res = []
    for i in sorted(ans):
        res.append(ans[i])
    return res
