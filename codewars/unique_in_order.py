# https://www.codewars.com/kata/54e6533c92449cc251001667/
def unique_in_order(iterable):
    n = len(iterable)
    arr = []
    if not iterable:
        return []
    if n <= 1:
        return [iterable]
    elif n == 2:
        if iterable[0] != iterable[1]:
            return [iterable[0], iterable[1]]
        return [iterable[0]]
    else:
        for i in range(n - 1):
            if iterable[i] != iterable[i + 1]:
                arr.append(iterable[i])
        if iterable[-1] != arr[-1]:
            arr.append(iterable[-1])
        return arr
