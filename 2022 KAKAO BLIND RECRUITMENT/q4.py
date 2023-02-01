from itertools import combinations_with_replacement
def solution(n, info):
    val = 0
    ans = []
    for i in combinations_with_replacement(range(11),n):
        cur = [0,0,0,0,0,0,0,0,0,0,0]
        a_score = 0
        l_score = 0
        for score in i:
            cur[score]+=1
        for score,num in enumerate(cur):
            if num>info[10-score]:
                l_score+=score
            elif info[10-score] != 0:
                a_score+=score
        if val < (l_score-a_score):
            ans = cur
            val = l_score-a_score
    return ans[::-1] if ans else [-1]