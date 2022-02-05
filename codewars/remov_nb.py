# https://www.codewars.com/kata/5547cc7dcad755e480000004
def remov_nb(n):
    arr = []
    needed = n * (n + 1) / 2
    for a in reversed(range(n)):
        b = (needed - a) / (a + 1)
        if b > n:
            break
        if (needed - a) % (a + 1) == 0:
            arr.append((round(b), a))
    return arr
