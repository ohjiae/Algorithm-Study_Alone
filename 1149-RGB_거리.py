# [1149번 : RGB 거리](https://www.acmicpc.net/problem/1149)
# 🙋‍♀️ 내 코드
#import sys
#sys_input = sys.stdin.readline
num = int(input())
house = [list(map(int, input().split())) for _ in range(num)]

result = [[0]*3 for _ in range(num)]
# 첫번째 집 R,G,B
for k in range(3):
    result[0][k] = house[0][k]

def find_min(h):
    # 최소값으로 result 채우기.
    result[h][0] += min(house[h-1][1], house[h-1][2]) 
    result[h][1] += min(house[h-1][0], house[h-1][2]) 
    result[h][2] += min(house[h-1][0], house[h-1][1]) 
    print('R=' ,result[h][0] + min(house[h-1][1], house[h-1][2]),'G=',result[h][1] + min(house[h-1][0], house[h-1][2]),'B=',result[h][2] + min(house[h-1][0], house[h-1][1])) 

for i in range(1,num):
    find_min(i)

print('h=',house,'\nr=',result)