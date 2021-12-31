# [10809번 : 알파벳 찾기](https://www.acmicpc.net/problem/10809)
# 🙋‍♀️ 내 코드

S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
result = []
for a in alpha :
    result.append(S.find(a))
print(*result, sep = ' ')
