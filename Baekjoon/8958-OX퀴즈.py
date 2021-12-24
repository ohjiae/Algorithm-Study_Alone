# [8958번 : OX퀴즈](https://www.acmicpc.net/problem/8958)
# 🙋‍♀️ 내 코드

import sys
num = int(input())
OX_line = []
for _ in range(num):
    OX_line.append(sys.stdin.readline().strip().split('X'))
for OX in OX_line:
    sum = 0
    for i in OX:
        n = len(i)
        sum += ((n**2)+n)/2 #삼각수 공식
    print(int(sum))
           

# 더 짧게 줄여보자

import sys
OX_line = [list(map(str,sys.stdin.readline().strip().split('X'))) for _ in range(int(input()))]
for OX in OX_line:
    sum = 0
    for i in OX:
        n = len(i)
        sum += ((n**2)+n)/2 #삼각수 공식
    print(int(sum))

   # 더 빠르진않음 ㅠ