# [8958λ² : OXν΄μ¦](https://www.acmicpc.net/problem/8958)
# πββοΈ λ΄ μ½λ

import sys
num = int(input())
OX_line = []
for _ in range(num):
    OX_line.append(sys.stdin.readline().strip().split('X'))
for OX in OX_line:
    sum = 0
    for i in OX:
        n = len(i)
        sum += ((n**2)+n)/2 #μΌκ°μ κ³΅μ
    print(int(sum))
           

# λ μ§§κ² μ€μ¬λ³΄μ

import sys
OX_line = [list(map(str,sys.stdin.readline().strip().split('X'))) for _ in range(int(input()))]
for OX in OX_line:
    sum = 0
    for i in OX:
        n = len(i)
        sum += ((n**2)+n)/2 #μΌκ°μ κ³΅μ
    print(int(sum))

   # λ λΉ λ₯΄μ§μμ γ 