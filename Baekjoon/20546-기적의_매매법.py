m = int(input())
p = list(map(int,input().split()))
def BNP(m,p):
    s = 0 
    for i in range(len(p)-1):
        if m>=p[i]:
            s += m//p[i]
            m = m%p[i]
    return p[-1]*s+m
def T(m,p):
    s = 0
    for i in range(3,len(p)):
        if p[i-1]<p[i-2]<p[i-3] and m >= p[i]:
            s += m//p[i]
            m = m%p[i]
        elif p[i-1]>p[i-2]>p[i-3] and s>0:
            m += s*p[i]
            s = 0 
    return p[-1]*s+m
if BNP(m,p)>T(m,p): print('BNP')
elif BNP(m,p)<T(m,p): print('TIMING')
else: print('SAMESAME')