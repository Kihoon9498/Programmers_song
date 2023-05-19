def solution(numbers, n):
    answer = 0
    while answer <= n:
        answer += numbers.pop(0)
    return answer