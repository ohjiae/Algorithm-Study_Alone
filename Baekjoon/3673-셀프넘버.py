# [3673번 : 셀프넘버](https://www.acmicpc.net/problem/3673)
# 🙋‍♀️ 내 코드
def d(n):
    num = n + sum(map(int,str(n)))
    return num
nn = set(range(1,10001))
for i in range(1,10001):
    nn.discard(d(i))
print(*nn,sep ='\n')
