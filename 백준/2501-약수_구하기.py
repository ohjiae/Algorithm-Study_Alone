#[2501번](https://www.acmicpc.net/problem/2501)
# 🙋‍♀️ 내 풀이

N, K = map(int,input().split())
k_list = []
for q in range(1,N+1):
    if (N%q == 0) : k_list.append(q)
try : print(k_list[K-1])
except : print(0)


# 👩‍💻 다른 사람 풀이 [sane2710님](https://www.acmicpc.net/source/14350609)

a, b = map(int, input().split())
c = [i for i in range(1, a+1) if a%i==0]
print(0 if len(c)<b else c[b-1])