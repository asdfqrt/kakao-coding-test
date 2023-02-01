import math

def solution(n, k):
    def convert(num,base):
        tmp = ""
        while num:
            tmp = str(num%base) + tmp
            num //= base
        return tmp
    def prime(num):
        if num==1: return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0: return False
        return True
    
    arr = convert(n,k)
    res = 0
    for num in arr.split("0"):
        if not num.isdigit(): continue
        if prime(int(num)):
            res+=1
    return res




print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]	))
print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]	))