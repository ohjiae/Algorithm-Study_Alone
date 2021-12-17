# 3회차

> **문제 ** <br>
1. [Task Hare](https://binarysearch.com/problems/Task-Hare)<br>
2. [Maximum Number by Inserting Five](https://binarysearch.com/problems/Maximum-Number-by-Inserting-Five)<br>
3. [123 Number Flip](https://binarysearch.com/problems/123-Number-Flip)<br>
4. [Social Distancing](https://binarysearch.com/problems/Social-Distancing)<br>

<br>
오늘 처음으로 시간내에 1개는 속도 1ms로 풀고, 나머지 한문제도 90%정도 풀었다..! 점점 늘고 있는게 느껴져서 너무 기분이 좋다.<br>
<p>
+ 오늘 **Flag의 개념**에 대해 배웠다. <br>
Flag기능은 For문 내에서 반복을 다 돌고나서도 조건이 만족되지않아 그냥 빠져나온 경우, Boolean인 Flag 변수를 줘서 그 이후에 어떻게 할 것인지 행동을 정해주는 것이다!<br>
(예시 : 변화 전 - Flag = False, 변화 후 - Flag = True)<br>
- 파이썬에서는 Flag 대신 For, Else 구문으로 쓰기도하지만 차이점이 있다. <br>
**Flag + break :** 변화가 일어났을때 멈추고 싶다면, Flag 값을 바꾼뒤에 Break로 빠져나온다. <br>
**For, Else :** 중간에 멈추지않고 For문이 다 돌고 Else 구문으로 넘어간다.<br>

## 1. Task Hare
<br>
이 문제... 정말 날 너무 힘들게한다.. 지금 푼 문제들 중 가장 오래걸림.. 엣지케이스가 너무 많아요.. <br>
하지만.. 내가 이길 것이다..! 풀고 만다! <br>
- 🙋‍♀️ 내 코드 (진행중)
```python
class Solution:
    def solve(self, n):
        n = str(n)
        num = []
        for i in range(len(n)):
            num.append(n[i])
        if num[0] == '-':
            flag = False
            for i in range(1,len(num)):
                if int(num[i])>5 :
                    num.insert(num.index(num[i]), 5)
                    flag = True
                    break
            if flag == False :
                num.append(5)

            num = ''.join(map(str,num[1:]))
            return(-int(num))
        else :
            flag = False
            for i in range(len(num)):
                if int(num[i])<5 :
                    num.insert(num.index(num[i]), 5)
                    flag = True
                    break
            if flag == False : 
                num.insert(num[-1],5)
            num = ''.join(map(str,num))
            return(int(num))
        
```

## 2. Maximum Number by Inserting Five
<br>
- 🙋‍♀️ 내 코드
```python
class Solution:
    def solve(self, n):
        n = str(n)
        num = []
        for i in range(len(n)):
            num.append(int(n[i]))
        for i in range(len(n)):
            if num[i]<3 :
                num[i] = 3
                break
        num = ''.join(map(str,num))   
        return(int(num))


```

## 3. 123 Number Flip
<br>
96%의 속도로 처음 푼 문제!(뿌듯)😎
<br>
- 🙋‍♀️ 내 코드
```python
class Solution:
    def solve(self, n):
        n = str(n)
        num = []
        for i in range(len(n)):
            num.append(int(n[i]))
        for i in range(len(n)):
            if num[i]<3 :
                num[i] = 3
                break
        num = ''.join(map(str,num))   
        return(int(num))


```

## 4. Social Distancing
<br>
- 🙋‍♀️ 내 코드
```python

```
