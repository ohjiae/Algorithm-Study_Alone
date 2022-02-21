# 문제 - 1이 될 때까지 : 답안 예시
# (나동빈 <이코테 2021 강의 2.그리디 & 구현> 15:55 ~)
# 어떤 수 N과 K가 주어지면, N을 1이 될 때까지 걸리는 연산 횟수의 최소한을 구하는 문제.
# N을 줄이는 방법은 단 2가지, 1. K로 나눈다. 2. N에서 1을 뺀다. 


# N, K을 공백으로 기준으로 구분하여 입력 받기
# N, K = map(int, input().split())
N, K = 26, 3
result = 0
while_count = 0

while True :
    while_count += 1
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N//K) * K 
    result += (N - target) # 1회차 : N이 26이었는데 나눌수있는 24로 변했으니 그 차수인 2만큼 -1 한걸로 치고 result(연산 수)값에 추가하는 과정.
    N = target # 횟수 추가했으니 나눌수 있는 값으로 변경.
    print(f'while 1단계 * {while_count}\n N = {N}, K = {K}, r = {result}, t = {target} ')
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 탈출
    # 나눌 수 있는지 없는지 먼저 판별 후 나누기.
    if N < K :
        break
    # K로 나누기
    result += 1 # 2 += 1. result = 3
    print(f'while 2단계 * {while_count}\n N = {N}, K = {K}, r = {result}, t = {target} ')
    N //= K # 0?
    print(f'while 3단계 * {while_count}\n N = {N}, K = {K}, r = {result}, t = {target} ')

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (N-1) 
print(f'while끝, 최종 : N = {N}, K = {K}, r = {result}')
    
'''
while 1단계 * 1
 N = 24, K = 3, r = 2, t = 24 
while 2단계 * 1
 N = 24, K = 3, r = 3, t = 24 
while 3단계 * 1
 N = 8, K = 3, r = 3, t = 24 
while 1단계 * 2
 N = 6, K = 3, r = 5, t = 6 
while 2단계 * 2
 N = 6, K = 3, r = 6, t = 6 
while 3단계 * 2
 N = 2, K = 3, r = 6, t = 6 
while 1단계 * 3
 N = 0, K = 3, r = 8, t = 0 
while끝, 최종 : N = 0, K = 3, r = 7
'''
