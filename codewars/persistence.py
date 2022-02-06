# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n):
    st = str(n)
    c = 0
    while len(st) > 1:
        mult = 1
        c += 1
        for i in st:
            mult *= int(i)
        st = str(mult)
    return c
