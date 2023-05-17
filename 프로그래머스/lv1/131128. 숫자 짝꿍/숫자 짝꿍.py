from collections import Counter


def solution(X, Y):
    answer = ""
    X = Counter(X)
    Y = Counter(Y)

    for i in range(9, -1, -1):
        mn = min(X[str(i)], Y[str(i)])
        answer += str(i) * mn

    # 겹치는게 없는 경우
    if answer == "":
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer