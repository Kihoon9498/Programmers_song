def solution(n, t, m, p):
    num, data, trans = 0, "0", {k:v for k,v in zip(range(16),"0123456789ABCDEF")}

    while len(data) < m*(t+1)+1:
        num,i,R = num+1, num+1, []
        while i!=0:
            R.append(i%n)
            i //= n            
        data += "".join([trans[r] for r in R][::-1])

    return data[p-1::m][:t]