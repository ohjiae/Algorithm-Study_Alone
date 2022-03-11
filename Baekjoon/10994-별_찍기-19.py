n=int(input())
star = [[' ' for _ in range(n*4-3)] for _ in range(n*4-3)]

def draw(num,index):
    l = num*4-3
    if num == 1:
        star[index][index] = '*'
    else:
        for j in range(l):
            star[index][j+index] = '*'
            star[j+index][index] = '*'
            star[index+l-1][j+index]= '*'
            star[j+index][index+l-1] = '*'          

idx = 0
if n == 1:
    draw(1,idx)
else:
    for i in range(n,0,-1):
        draw(i,idx)
        idx += 2

print(*list(''.join(s) for s in star), sep='\n')