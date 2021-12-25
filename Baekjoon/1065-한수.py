# [1065번 : 한수](https://www.acmicpc.net/problem/1065)
# 🙋‍♀️ 내 코드

n = int(input())
cnt = 99
if n < 100:
    print(n)
else : 
    for i in range(100,n+1):
        han = list(map(int, str(i)))
        if han[0]-han[1] == han[1]-han[2]:
            cnt += 1
    print(cnt)
    
