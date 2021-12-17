# 2회차
> **문제**<br>
1.[Detect the Only Duplicate in a List](https://binarysearch.com/problems/Detect-the-Only-Duplicate-in-a-List)<br>
2.[Median Minimization](https://binarysearch.com/problems/Median-Minimization)<br>
3.[Buying Cars](https://binarysearch.com/problems/Buying-Cars)<br>
4.[Max Product of Three Numbers](https://binarysearch.com/problems/Max-Product-of-Three-Numbers)<br>

## 1. Detect the Only Duplicate in a List

- 🙋‍♀️  내 코드
```python
class Solution:
    def solve(self, nums):
        n = int(len(nums)-1)
        return(sum(nums) - int(n*(n+1)/2))
```
처음에는 for문으로 ```nums.count(nums[i]) == 2``` 인 경우를 찾으려고 했더니 시간초과가 났다.<br>
그리고 나서 보너스인 O(n)이 아닌 O(1)으로 풀 수 있다고 해서 다시 고민 했지만, 시간 내에는 풀지 못했다.<br>
이후 좀 더 수학적으로 접근해야 하는 것을 알게 되었다. <br>
결국 nums = nums의 합 + 추가된 하나의 i이므로,<br>
nums의 합을 왼쪽 항으로 옮기면 i를 쉽게 구할 수 있다.<br>
그래서 등차수열의 합 공식을 사용해 풀었다.<br>
<br>
무작정 문제를 옮겨 적는 것이 아니라, 왜 수학적으로 접근해야 하는지, 왜 일반화를 시키며 문제를 풀어야 하는지 알게 된 아주 좋은 순간이었다.
<br>
## 2. Median Minimization

- 🙋‍♀️  내 코드
```python
class Solution:
    def solve(self, nums):
        nums = sorted(nums)
        left = []
        right = []
        for i in range(0,len(nums),2):
            left.append(nums[i])
            right.append(nums[i+1])
        l = int(round(len(left)/2))
        return(abs(left[l-1] - right[l-1]))
```
속도는 느리지만... 만들긴했다.. 나중에 고수가 되면 더 효율적이고 빠르게 짤 수 있겠지..?

## 3. Buying Cars

- 🙋‍♀️  내 코드
```python
class Solution:
    def solve(self, prices, k):
        prices.sort()
        count = 0
        for i in prices :
            if k - i >= 0 :
                k = k - i
                count += 1
        return(count)
```

이것 또한 단순하게 생각해야 풀 수 있는 문제였다..<br>
오늘 이후로 문제 옮겨 적듯 쓰는 코드는 하지 않을 것이다..!<br>
## 4. Max Product of Three Numbers

- 🙋‍♀️  내 코드
```python
class Solution:
    def solve(self, nums):
        nums = sorted(nums)
        print(nums)
        return(max(nums[0]*nums[1]*nums[2],nums[-3]*nums[-2]*nums[-1]))

    # Edge case
    # nums = [-3, 4, -4, 0]
    # 다른사람 코드 찾기.
```

이건 공부가 필요하다...
