def solution(participant, completion):
    participant.sort()
    completion.sort()
    if len(participant) == 1:
        answer = participant[0]
    while completion:
        comp = completion.pop()
        part = participant.pop()
        if comp != part:
            answer = part
            break
        if len(participant) == 1:
            answer = participant[0]
            break
    return answer