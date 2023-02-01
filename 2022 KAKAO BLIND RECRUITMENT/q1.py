def solution(id_list, report, k):
    res = {id : set() for id in id_list}
    ans = {id :0 for id in id_list}
    a =[]
    for string in report:
        ppl, target = string.split()
        res[target].add(ppl)
    for id in res:
        if len(res[id]) >=k:
            for ppl in res[id]:
                ans[ppl]+=1
    for i in ans.values():
        a.append(i)
    return a