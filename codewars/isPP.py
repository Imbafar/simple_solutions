# https://www.codewars.com/kata/54d4c8b08776e4ad92000835
def isPP(n):
    for i in range(2, n // 2 + 1):
        c = 0
        flag = False
        m = n
        while m % i == 0:
            m = m / i
            c += 1
            if m == 1:
                flag = True
                break
        if flag:
            return [i, c]
