# 백준 문제, 기본부터 최다 빈출 문제까지 풀기
 ## 준비운동 Part1. 튼튼한 기본기

> 코딩테스트를 대비하며 여러 문제를 풀고자 합니다.
코테 연습용 문제는 매우 많으므로, 좋은 문제들만 엄선한 포스팅을 따라 순서대로 풀겠습니다.
이번에 따라할 문제 로드맵은 이곳입니다.
[Covernant님 로드맵](https://covenant.tistory.com/224)

### 1. 약수 구하기 (🥉 브론즈 3티어, [2501번](https://www.acmicpc.net/problem/2501))
**문제**
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 
6을 예로 들면 6의 약수는 1, 2, 3, 6, 총 네 개이다. 
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
**입력**
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.
**출력**
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.


- 내 풀이
```python
N, K = map(int,input().split())
k_list = []
for q in range(1,N+1):
    if (N%q == 0) : k_list.append(q)
try : print(k_list[K-1])
except : print(0)
```
- 더 나은 남의 풀이 [sane2710님] (https://www.acmicpc.net/source/14350609)
```python
a, b = map(int, input().split())
c = [i for i in range(1, a+1) if a%i==0]
print(0 if len(c)<b else c[b-1])

```

### 2. 이진수 (🥉 브론즈 3티어, [3460번](https://www.acmicpc.net/problem/3460))
**문제**
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.

**입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)

**출력**
각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.

- 내 풀이
```python

```

### 3. 최소, 최대 (🥉 브론즈 3티어, [10818번](https://www.acmicpc.net/problem/10818))
**문제**

**입력**

**출력**

- 내 풀이
```python

```

### 4. 지능형 기차 2 (🥉 브론즈 3티어, [2460번](https://www.acmicpc.net/problem/2460))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
### 5. 피보나치 수 5 (🥉 브론즈 2티어, [10870번](https://www.acmicpc.net/problem/10870))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
### 6. 일곱 난쟁이 (🥉 브론즈 2티어, [2309번](https://www.acmicpc.net/problem/2309))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
### 7. 최대공약수와 최소공배수 (🥈실버 5티어, [2609번](https://www.acmicpc.net/problem/2609))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
### 8. N번째 큰 수 (🥈실버 5티어, [2693번](https://www.acmicpc.net/problem/2693))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
### 9. 소수 찾기 (🥈실버 4티어, [1978번](https://www.acmicpc.net/problem/1978))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
### 10. 쉽게 푸는 문제 (🥈실버 4티어, [1292번](https://www.acmicpc.net/problem/1292))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
### 11. 소수 (🥈실버 4티어, [2581번](https://www.acmicpc.net/problem/2581))
**문제**

**입력**

**출력**

- 내 풀이
```python

```
