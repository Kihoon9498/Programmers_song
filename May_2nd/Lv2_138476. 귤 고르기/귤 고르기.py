def solution(k, tangerine):
    answer = 0
    temp = {}
    # set으로 중복을 제거하여 count한 값들을 저장하려 하였으나 시간 초과로 문제가 발생하여 하나씩 확인하는 방법으로 변경함
    for i in tangerine:
        if i in temp:
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1
    # 딕셔너리의 values를 리스트로 변경하고 정렬하여 값을 계산
    temp = list(temp.values())
    temp.sort(reverse=True)
    while k > 0:
        k -= temp.pop(0)
        answer += 1
    return answer