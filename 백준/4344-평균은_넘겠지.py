# [4344번 : 평균은 넘겠지](https://www.acmicpc.net/problem/4344)
# 🙋‍♀️ 내 코드

import sys
n = int(input())
for _ in range(n):
    st_num, *scores = map(int,sys.stdin.readline().split())
    print('%.3f' %(sum(scores)/st_num)+'%')