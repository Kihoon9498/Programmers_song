import math

def solution(n):
    answer = 0
    for i in range(n):
        # math 라이브러리의 comb함수를 이용하여 계산함
        # 다른 사람의 풀이를 보니 피보나치 수열로 계산하는 과정도 있었음
        answer += math.comb(n-i, i)
        if n-i <= i:
            break
    return answer % 1234567