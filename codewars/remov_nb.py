# https://www.codewars.com/kata/5547cc7dcad755e480000004
from audioop import reverse
import time


def remov_nb(n):
    needed = (n)/2*(n+1)
    # print(needed)
    for a in reversed(range(n)):
        for b in reversed(range(a, n+1)):
            # print(a+1, b)
            test = a*b + a + b
            if needed == test:
                return [(a, b), (b, a)]
    return []
# 1000003


start = time.perf_counter()
print(remov_nb(101))
print(time.perf_counter() - start)
