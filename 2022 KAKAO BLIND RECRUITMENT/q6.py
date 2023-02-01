

def solution(board, skill):
    n = len(board)
    m = len(board[0])
    change = [[0]*m for _ in range(n)]
    ans = 0
    for type,x1,y1,x2,y2,degree in skill:
        if type==1: degree *= -1
        change[x1][y1] += degree
        if y2<m-1:
            change[x1][y2+1] -= degree
        if x2<n-1:
            change[x2+1][y1] -= degree
        if x2<n-1 and y2<m-1:
            change[x2+1][y2+1] += degree
    for x in range(n):
        for y in range(m):
            if x>0:
                change[x][y] += change[x-1][y]
            if y>0:
                change[x][y] += change[x][y-1]
            if x>0 and y>0:
                change[x][y] -= change[x-1][y-1]
            
            if board[x][y] + change[x][y] >0:
                ans+=1
    return ans


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
