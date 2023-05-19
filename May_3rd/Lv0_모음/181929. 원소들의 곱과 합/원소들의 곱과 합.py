def solution(num_list):
    mul_n = 1
    for i in num_list:
        mul_n *= i
    return 1 if mul_n < (sum(num_list)**2) else 0