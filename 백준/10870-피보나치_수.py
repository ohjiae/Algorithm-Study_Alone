# [10870번 : 피보나치 수](https://www.acmicpc.net/problem/10870)
# 🙋‍♀️ 내 코드

n = int(input())
fib = [0,1]
for i in range(2,n+1):
    num = fib[i-1]+fib[i-2]
    fib.append(num)
print(fib[n])


# 👩‍💻 다른 사람 코드 (내가 하려던 코드)

def p(n):
    x=0
    y=1
    for i in range(n):
        x,y=y,x+y;
    return x
a=int(input())
print(p(a))

# 👩‍💻 다른 사람 코드 2

def r(x):
    if x < 2: return x
    return r(x-1)+r(x-2)
print(r(int(input())))