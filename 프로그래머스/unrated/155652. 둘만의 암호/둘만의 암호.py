def solution(s, skip, index):
    answer = ''
    engs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in skip:
        engs.pop(engs.index(i))

    for i in s:
        temp = ''
        try:
            temp = engs[engs.index(i) + index]
        except:
            temp = engs[(engs.index(i) + index) % len(engs)]
        answer += temp
    return answer