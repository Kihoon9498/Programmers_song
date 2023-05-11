def solution(n, m, section):
    answer = 0
    while section:
        temp_list = list(range(section[0], section[0] + m))
        while len(section) > 0 and section[0] <= temp_list[-1]:
            section.remove(section[0])
        answer += 1
    return answer