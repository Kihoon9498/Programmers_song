def solution(keymap, targets):
    answer = []
    for target in targets:
        new_list = []
        for key in keymap:
            temp = []
            for i in target:
                try:
                    temp.append(key.index(i)+1)
                except:
                    temp.append(999)
                    pass
            new_list.append(temp)
        min_list = new_list[0]
        count = 0
        while count < len(new_list):
            count += 1
            for n, i in enumerate(min_list):
                if count < len(new_list) and  new_list[count][n] < i:
                    min_list[n] = new_list[count][n]
        if 999 in min_list:
            answer.append(-1)
        else:
            answer.append(sum(min_list))
    return answer