# 풀지 못한 문제 풀이

# 기타 코딩

- where(조건, A, B) → 조건이 참이면 A, 거짓이면 B
- rjust : 오른쪽으로 정렬
- ljust : 왼쪽으로 정렬
- zfill : 왼쪽에 0을 채워줌

# 1. 숨어있는 숫자의 덧셈(1)

```python
import re
my_string = "aAb1B2cC34oOp"
answer = 0
num = re.findall(r"\d", my_string) # re 라이브러리의 findall함수 -> 매치된 부분의 문자열을 리스트로 도출, \d --> 숫자와 매치
for i in num:
    answer += int(i)

print(answer)
```

# 2. 순서쌍의 개수

```python
n = 20
answer = 0
for i in range(1, n+1):
    if n % i == 0:
        answer += 1

print(answer)
```

# 3. 대문자와 소문자

```python
my_string = "cccCCC"
answer = ''
for i in my_string:
    if i.isupper(): # 문자가 대문자인지 소문자인지 확인해주는 함수 / is upper?
        answer += i.lower()
    else:
        answer += i.upper()
```

# 4. 숨어있는 숫자의 덧셈(2)

```python
import re

my_string = "aAb1B2cC34oOp"
answer = 0
numbers = re.findall(r'\d+', my_string) # re라이브러리의 findall함수 -> \d+ => 1회 이상 반복되는 숫자들에 대한 패턴
for i in numbers:
    answer += int(i)
answer
```

# 다른 사람의 풀이

```python
s = ''.join(i if i.isdigit() else ' ' for i in my_string)
answer = sum(int(i) for i in s.split())
```

# 5. 영어는 싫어요

numbers = "onetwothreefourfivesixseveneightnine"

# 다른 사람의 풀이

```python
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
```

# 6. 문자열 계산하기

```python
my_string = "3 - 0 + 41 - 12"

strs = my_string.split(' ')
sum = int(strs[0])
for i, n in enumerate(strs):
    if i % 2 != 0:
        if strs[i] == '+':
            sum += int(strs[i+1])
        else:
            sum -= int(strs[i+1])
print(sum)
```

# 다른 사람의 풀이

```python
def solution(my_string):
    return eval(my_string) # 문자열 그대로를 계산하는 것
```

# 7. 치킨 쿠폰

```python
chicken = 1081

answer = 0
while chicken >= 10:
    div, mod = divmod(chicken, 10)
    answer += div
    chicken = div+mod

print(answer, chicken)
```

# 다른 사람의 풀이

```python
def solution(chicken):
    return int(chicken*0.11111111111)
```

# 8. 유한소수 판별하기

## 억지로 풂...

```
answer = 0
    strs = str(a/b).split('.')
    if len(strs[1]) > 10:
        answer = 2
    else:
        answer = 1
```

# 다른 사람의 풀이

```python
from math import gcd # 최대공약수 함수
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
```

# 9. 특이한 정렬

```
numlist = [1, 2, 3, 4, 5, 6]
n = 4
```

# 다른 사람의 풀이

```python
difference = [num - n for num in numlist]
distance = [num - n if num - n >= 0 else n - num for num in numlist]    
distance.sort()

    # 반복되는 숫자가 나올경우 뒤에 숫자를 음수로 변환
for idx in range(len(distance)-1):
    if distance[idx] == distance[idx+1]:
        distance[idx+1] = -distance[idx]

for idx in range(len(distance)):
    if distance[idx] not in difference:
        distance[idx] = -distance[idx]

answer = [d+n for d in distance]
```

# 10. 분수의 덧셈

```
numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4

mo = numer1 * numer2
ja = denom1 * numer2 + denom2 * numer1
start = max(mo, ja)
gcd_value = 1

for num in range(start, 0, -1):
    if mo % num == 0 and ja % num == 0:
        gcd_value = num
        break

answer = [int(ja / gcd_value), int(mo / gcd_value)]
answer
```

# 다른 사람의 풀이

```python
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num) # gcd -> 최대공약수 함수
    return [denum//gcd, num//gcd]
```

# 11. 안전지대

```
from collections import deque

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

def solution(board):
    dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x, y): # bfs : Breadth First Search, 너비 우선 탐색
        dq = deque()
        dq.append((x, y))
        while dq:
            a, b = dq.popleft()
            visited[a][b] = True
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                #위험지역으로 둬야함 
                if 0<=nx<length and 0<=ny<length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        dq.append((nx, ny))
                    else:
                        board[nx][ny] = 2 #위험지역 처리 

    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i, j)
    result = 0
    for i in range(length):
        result += board[i].count(0)
    return result
```

# 다른 사람 간단 풀이

```
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
```

# 12. 옹알이(1)

```python
#옹알이1을 해결해보았따
def solution(babbling):
    bab_list = ['aya', 'ye', 'woo', 'ma']
    bab_f_list = ['a','y','w','m']
    answer = len(babbling)
    for i in babbling:
        while i:
            if i[0] in bab_f_list and i[:len(bab_list[bab_f_list.index(i[0])])] == bab_list[bab_f_list.index(i[0])]:
                temp_len = len(bab_list[bab_f_list.index(i[0])])
                i = i[temp_len:]
            else:
                answer -= 1
                break
    return answer
```

```python
babbling = ["aya", "yee", "u", "maa", "wyeoo"]

def solution(babbling):
    answer = 0
    for i in babbling:
        for j in [ "aya", "ye", "woo", "ma" ]:
            if j * 2 not in i:
                i = i.replace(j, ' ')
        if len(i.strip()) == 0:
            answer += 1
    return answer
```

# Lv1

## 1. 문자열 내마음대로 정하기

```python
strings = ["sun", "bed", "car"]
n = 1

answer = []
for i in range(len(strings)):
    strings[i] = strings[i][n] + strings[i]
strings.sort()

for i in range(len(strings)):
    answer.append(strings[i][1:])
```

## 2. 옹알이(2)

```python
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if not i.rstrip():
            answer +=1
    return answer
```

# Lv2

## 1. 예상 대진표

```python
# 나의 풀이
n = 8
a = 4
b = 7
temp = sorted([a, b])
answer = 0
while True:
    answer += 1
    if temp[1] % 2 == 0 and temp[0] == (temp[1]-1):
        break
    else:
        temp[0] = (temp[0] + 1) // 2
        temp[1] = (temp[1] + 1) // 2
answer

# 다른 사람의 풀이

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length() # 
```

## 2. 점프와 순간이동

```python
n = 5
# 다른 사람의 풀이

def solution(n):
    answer = 0
    while n>0:
        n, i = divmod(n, 2)
        if i != 0:
            answer += 1
    return answer

# 다른 사람 간단 풀이
def solution(n):
    return bin(n).count('1')
```
