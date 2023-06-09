def solution(s):
    l_s = ['[', '{', '(']
    r_s = [']', '}', ')']
    right = ['[]', '{}', '()']

    answer = 0
    for i in range(len(s)):
        if len(s) % 2 != 0:
            break
        temp = s[i:] + s[:i]
        if temp[0] in r_s:
            continue
        count = 0
        while right[0] in temp or right[1] in temp or right[2] in temp:
            if temp[count] + temp[count + 1] in right:
                temp = temp[:count] + temp[count+2:]
                count = 0
                if len(temp) == 0:
                    answer += 1
                    break
            else:
                count += 1
    return answer