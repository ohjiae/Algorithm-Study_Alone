알고리즘 문제를 푸는 스터디를 시작했습니다!<br>
Binary search 사이트를 활용했으며, 시간 내에 4가지 문제를 푸는 스터디입니다.<br>
(여담으로 이 사이트 너무 좋아요... 보여진 테스트 케이스 외에 여러 가지 극한의 테스트 케이스도 주어져서, 어떤 상황에서도 작동이 되야만 정답이 됩니다)<br>

> **오늘 진행한 문제**<br>1. [Wolf of Wall street](https://binarysearch.com/problems/Wolf-of-Wall-Street)
<br>2. [Shortest Sublist With Max Frequency](https://binarysearch.com/problems/Shortest-Sublist-With-Max-Frequency)
<br>3. [Consecutive Ones](https://binarysearch.com/problems/Consecutive-Ones)
<br>4. [Mutual Followers](https://binarysearch.com/problems/Mutual-Followers)

<p>
1. Wolf of Wall street <br>
- 내 코드<br>
    
    
```python
class Solution:
    def solve(self, prices):
        if len(prices)==0:
            return(0)
        buy = min(prices)
        i = prices.index(buy)
        del prices[:i]

        sell = max(prices)
        if buy<sell:
            return(sell-buy)
        else :
            return(0)
```
                     
<br>                     
제 코드는 최소값(주식을 살 가격)을 찾고 그 전의 모든 가격은 지워버리는 식이었습니다.<br>
그랬더니 테스트케이스가 prices = [1, 2, 0] 일 때, <br>
1에서 사고 2에서 팔아 얻을 수 있는 1도 얻지 못하고 0 이전의 원소들을 다 지워버려서 문제가 생겼습니다.<br>

<p>
시간 초과로 더 풀지 못했지만 저희 스터디의 가장 고수분께서... 각 문제와 관련된 알고리즘을 알려 주셨습니다.<br>

> 1번 문제는 Kadane’s Algorithm
2,3번은 Array 문제
4번 문제는 전형적인 그래프문제


그래서 오늘은 Kadane's Algorithm에 대해 공부하고 TIL을 업로드하겠습니다! 

**[Kadane's Algorithm 에 관한 TIL 바로가기]()**

3. Consecutive Ones<br>
의지의 오지애..... 4시간 걸려서 풀었다.... 이렇게 간단해 보이는게 오래걸리다니 ㅠㅠㅠㅠ<br>
공부 열심히하자...<br>
```python
class Solution:
    def solve(self, nums):
        ones = []
        for i in range(len(nums)):
            if nums[i] == 1 :
                ones.append(1)
            else : ones.append(0) #1과 1이 아닌 수로 구분
        if len(nums)>1 : # 원소가 1개 이상일 때 / 아래조건: 하나 일 때
            while ones[0] == 0 : #앞의 0제거
                del ones[0]
            while ones[-1] == 0 : #뒤의 0제거
                del ones[-1]
            # 시퀀스 분리
            ones = ''.join(list(map(str,ones))).split('0')
            max_i = []
            max_len = len(max(ones,key = len))
            if len(ones) == 1 : # 유일한 시퀀스
                return(True)
            else : # 시퀀스 여러개
                for i in range(len(ones)):
                    if int(len(ones[i])) == max_len:
                        max_i.append(ones[i]) #시퀀스 중 길이 최대인 것만 추가
                    else:
                        pass
                return(False)

        elif nums[0] == 1 : # 그 하나가 1일 때
            return(True)
        else : #그 하나가 1 아닐 때   
            return(False)     

```

