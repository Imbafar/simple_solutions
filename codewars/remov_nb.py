# https://www.codewars.com/kata/5547cc7dcad755e480000004
def remov_nb(n):
    arr = []
    needed = (n)/2*(n+1)
    flag = False
    for a in range(n+1):
        if flag:
            break
        for b in range(a):
            print(a,b)
            test = a*b + a + b
            if needed == test:
                arr.append((b,a))
                arr.append((a,b))
                flag = True
                break
    return arr

print(remov_nb(26))