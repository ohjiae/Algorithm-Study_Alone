# [2675번 : 문자열 반복](https://www.acmicpc.net/problem/2675)
# 🙋‍♀️ 내 코드
for _ in range(int(input())):
    R, S = map(str, input().split())
    result = []
    for a in S:
        result.append(a*int(R))
    print(*result,sep='')
