# [2581번 : 소수](https://www.acmicpc.net/problem/2581)
# 🙋‍♀️ 내 코드

M, N = [map(int,input().strip()) for _ in range(2)]

for i in (M,N+1):
    if i > 1 :
        for j in range(2,i+1):
            if i%j == 0:
                break
           