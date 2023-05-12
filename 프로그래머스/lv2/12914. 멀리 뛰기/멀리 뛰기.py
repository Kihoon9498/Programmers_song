import math

def solution(n):
    answer = 0
    for i in range(n):
        answer += math.comb(n-i, i)
        if n-i <= i:
            break
    return answer % 1234567