def solution(k, tangerine):
    answer = 0
    dict_tang = {}
    for tang in tangerine:
        if tang not in dict_tang:
            dict_tang[tang] = 1
        else:
            dict_tang[tang] += 1

    num_tang = sorted(list(dict_tang.values()), reverse=True)

    while k > 0:
        k -= num_tang[answer]
        answer += 1
    return answer