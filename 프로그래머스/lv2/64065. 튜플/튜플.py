def solution(s):
    answer = []
    s = s.replace('{', '')
    s_list = s.split('}')
    temp1 = []
    for i in s_list:
        if i != '':
            i = i.strip(',')
            temp1.append(i)

    temp2 = {}
    for j in temp1:
        temp = j.split(',')
        temp_len = len(temp)
        temp2[temp_len] = temp

    lens = sorted(list(temp2.keys()))
    sorted_list = []
    for j in lens:
        sorted_list.append(temp2[j])

    while sorted_list:
        temp = sorted_list.pop(0)
        i = 0
        while True:
            if int(temp[i]) not in answer:
                answer.append(int(temp[i]))
                break
            else:
                i += 1
    return answer