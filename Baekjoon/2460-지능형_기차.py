# [2460번 : 지능형 기차](https://www.acmicpc.net/problem/2460)
# 🙋‍♀️ 내 코드

import sys
train = [0]
for _ in range(10):
    i,j = map(int,sys.stdin.readline().split())
    train.append(train[-1] - i + j)
print(max(train))


# 👩‍💻 다른 사람 코드

import sys

current=0
maxpass=0
for i in range(10):
    A,B=map(int,sys.stdin.readline().split())
    current-=A
    current+=B
    if maxpass<current : maxpass=current
print(maxpass)