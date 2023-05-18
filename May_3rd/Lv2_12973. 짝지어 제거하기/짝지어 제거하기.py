def solution(s):
    temp = []
    for i in s:
        if i not in temp:
            temp.append(i)
        elif temp[-1] == i:
            temp.pop()
    return 1 if not temp else 0