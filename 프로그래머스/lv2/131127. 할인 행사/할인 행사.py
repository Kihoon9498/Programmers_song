def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - len(want)):
        temp_list = [0] * len(want)
        temp = discount[i:i+10]
        set_temp = set(temp)
        for i in set_temp:
            if i not in want:
                break
            else:
                temp_list[want.index(i)] += temp.count(i)
        if temp_list == number:
            answer += 1
    return answer