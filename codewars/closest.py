# https://www.codewars.com/kata/5868b2de442e3fb2bb000119
def closest(strng):
    if not strng:
        return []
    arr = [i for i in strng.split()]
    arr_num = []
    for i in arr:
        sum_num = 0
        for j in i:
            sum_num += int(j)
        arr_num.append(sum_num)
    arr = [int(i) for i in arr]
    n = len(arr)
    new_arr = sorted(list(zip(arr_num, range(n), arr)), key=lambda x: x[0])
    c = []
    i = 0
    while i + 1 < n:
        c.append(new_arr[i + 1][0] - new_arr[i][0])
        i += 1
    pos = c.index(min(c))
    return [[*new_arr[pos]], [*new_arr[pos + 1]]]
