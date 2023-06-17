def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        temp = (100 - progress) // speed
        if (100 - progress) % speed != 0:
            temp += 1
        days.append(temp)
    answer = []
    count = -1
    for day in days:
        if day > count:
            answer.append(1)
            count = day
        else:
            answer[-1] += 1
    return answer