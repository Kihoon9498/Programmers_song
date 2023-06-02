def solution(numbers, hand):
    answer = ''
    position = []
    l_hand = [3,0]
    r_hand = [3,2]
    for number in numbers:
        if number == 0:
            number = 11
        position.append([(number-1)//3, (number-1)%3])
        if number in [1,4,7]:
            l_hand = [(number-1)//3, (number-1)%3]
            answer += 'L'
        elif number in [3,6,9]:
            r_hand = [(number-1)//3, (number-1)%3]
            answer += 'R'
        else:
            l_dist = abs(position[-1][0] - l_hand[0]) + abs(position[-1][1] - l_hand[1])
            r_dist = abs(position[-1][0] - r_hand[0]) + abs(position[-1][1] - r_hand[1])
            if l_dist > r_dist:
                answer += 'R'
                r_hand = [(number-1)//3, (number-1)%3]
            elif l_dist < r_dist:
                answer += 'L'
                l_hand = [(number-1)//3, (number-1)%3]
            elif l_dist == r_dist and hand == 'right':
                answer += 'R'
                r_hand = [(number-1)//3, (number-1)%3]
            elif l_dist == r_dist and hand == 'left':
                answer += 'L'
                l_hand = [(number-1)//3, (number-1)%3]
    return answer