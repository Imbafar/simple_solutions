# https://www.codewars.com/kata/550f22f4d758534c1100025a/
def dirreduc(arr):
    DIRECT = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST",
    }
    i = 0
    while i + 1 < len(arr) and len(arr) >= 2:
        if arr[i] == DIRECT[arr[i + 1]]:
            arr.pop(i)
            arr.pop(i)
            i = 0
            continue
        i += 1
    return arr
