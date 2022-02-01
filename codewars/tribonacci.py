# https://www.codewars.com/kata/556deca17c58da83c00002db
def tribonacci(signature, n):
    a, b, c = signature
    arr = []
    arr += signature
    for i in range(n-3):
        c, b, a = a+b+c, c, b
        arr.append(c)
    return arr[:n]
