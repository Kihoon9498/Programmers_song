def solution(new_id):
    answer = 'A'
    for idx, i in enumerate(new_id):
        i = i.lower()
        if i.lower() == i.upper() and i not in ['-','_','.','0','1','2','3','4','5','6','7','8','9']:
            i = ''
        if i == '.' and answer[-1] == '.':
            i = ''
        answer += i
    answer = answer[1:]
    answer = answer.strip('.')
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.strip('.')
    elif len(answer) == 2:
        answer += answer[-1]
    elif len(answer) == 1:
        answer *= 3
    return answer