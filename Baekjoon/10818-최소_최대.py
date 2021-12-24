# [10818번 : 최소, 최대](https://www.acmicpc.net/problem/10818)
# 🙋‍♀️ 내 코드

from sys import stdin
N = int(input())
all = list(map(int,stdin.readline().split()))
print(all,min(all), max(all))


# 👩‍💻 다른 사람 코드

import sys
_, *n = map(int, sys.stdin.read().split())
print(min(n),max(n))
