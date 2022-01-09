# [10798번 : 세로 읽기](https://www.acmicpc.net/problem/10798)
    
  
import sys
from collections import deque
lines= [deque(list(sys.stdin.readline().strip())) for l in range(5)]
    
board = []
n = 0
for i in range(len(max(lines, key =len))):
    def add_n(n) :
        for line in lines:
            if n < len(line):
                board.append(line[n])
            else : pass
    add_n(n)
    n += 1
print(''.join(board))
  
