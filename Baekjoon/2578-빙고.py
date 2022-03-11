#import sys
#input = sys.stdin.readline
from collections import deque
cs = [list(map(int,input().split())) for _ in range(5)]
vis = [False for _ in range(12)]
def chk(cs):
    lcross = []
    rcross = []
    for i in range(5):
        if (vis[i] == False) and (any(cs[i]) == False): # 가로
            vis[i] = True
            if vis.count(True)>=3: 
                Flag = True
        vert = [cs[0][i],cs[1][i],cs[2][i],cs[3][i],cs[4][i]]
        if (vis[i+5] == False) and (any(vert)==False): # 세로
            vis[i+5] = True
            if vis.count(True)>=3: 
                Flag = True
        lcross.append(cs[i][i])
        rcross.append(cs[i][-(i+1)])

    if vis[10] == False: # 마지막에 체크
        if any(lcross) == False:
            vis[10] = True
            if vis.count(True)>=3: 
                Flag = True
    if vis[11] == False: # 오른쪽대각선 아직 빙고 아니면
        if any(rcross) == False:
            vis[11] = True
            if vis.count(True)>=3: 
                Flag = True
    return vis.count(True)
# 부르는거 받다가 10부터 체크 시작. 빙고가 만들어지면 출력.끝
call = [deque(map(int,input().split())) for _ in range(5)]
idx = 0
Flag = False
for line in call:
    while line and not Flag:
        idx += 1
        v = line.popleft()
        for c in cs:
            if v in c:
                c[c.index(v)] = False
                if idx >= 10:
                    bingo = chk(cs)
                    if bingo >= 3:
                        Flag = True
                        break
    if Flag == True : 
       print(idx)
       break
