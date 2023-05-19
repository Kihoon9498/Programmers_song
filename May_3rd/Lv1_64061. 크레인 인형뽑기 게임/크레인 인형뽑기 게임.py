def solution(board, moves):
    list_answer = []
    answer = 0
    for move in moves:
        loop = True
        while loop:
            count = 0
            for row in board:
                count += 1
                if row[move-1] != 0:
                    list_answer.append(row[move-1])
                    row[move-1] = 0
                    loop = False
                    break
            if count == len(board):
                break
    while True:
        count = 0
        n = len(list_answer)
        for i in range(n-1):
            count += 1
            if list_answer[i] == list_answer[i+1]:
                list_answer.pop(i)
                list_answer.pop(i)
                answer += 2
                break
        if count == (n-1):
            break
    return answer