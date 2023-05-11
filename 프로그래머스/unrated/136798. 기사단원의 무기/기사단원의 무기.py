def solution(number, limit, power):
    temp = []
    for i in range(1, number+1):
        num = 0
        for n in range(1, int(i**(1/2) + 1)):
            if i % n == 0 and n != i**(1/2):
                num += 2
            elif n == i ** (1/2):
                num += 1
        temp.append(num)
    answer = 0
    for i in temp:
            if i > limit:
                answer += power
            else:
                answer += i
    return answer