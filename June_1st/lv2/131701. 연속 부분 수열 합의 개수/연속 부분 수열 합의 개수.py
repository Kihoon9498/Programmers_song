def solution(elements):
    n = len(elements)
    temp = elements*2
    answer = []
    for i in range(n):
        for j in range(n):
            answer.append(sum(temp[i:i+(j+1)]))
    return len(set(answer))