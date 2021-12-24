# [3460번 : 이진수](https://www.acmicpc.net/problem/3460)
# 🙋‍♀️ 내 코드

T = int(input())
for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[::-1][i] == '1':
            print(i, end = ' ')


# 👩‍💻 다른 사람 코드

T = int(input())
for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i - 1] == '1':  # 이부분 다른 방법 (거꾸로 하나씩 세기)
            print(i, end = ' ')