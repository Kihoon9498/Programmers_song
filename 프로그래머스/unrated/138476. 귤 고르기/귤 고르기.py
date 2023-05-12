def solution(k, tangerine):
    answer = 0
    temp = {}
    for i in tangerine:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1

    temp = list(temp.values())
    temp.sort(reverse=True)
    while k > 0:
        k -= temp.pop(0)
        answer += 1
    return answer