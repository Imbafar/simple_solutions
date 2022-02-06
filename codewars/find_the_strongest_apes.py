# https://www.codewars.com/kata/617af2ff76b7f70027b89db3/
def find_the_strongest_apes(a):
    def comparator(first, second):
        f = first["weight"] + first["height"]
        s = second["weight"] + second["height"]
        if f != s:
            return f < s
        return first["name"] > second["name"]

    def srt(a):
        n = len(a)
        if n == 1:
            return a[0]
        for i in range(n - 1):
            for j in range(n - i - 1):
                if comparator(a[j], a[j + 1]):
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a[0]

    arr_gor = []
    arr_gb = []
    arr_or = []
    arr_ch = []

    for i in a:
        typ = i.get("type")
        if typ == "Gorilla":
            arr_gor.append(i)
        if typ == "Gibbon":
            arr_gb.append(i)
        if typ == "Orangutan":
            arr_or.append(i)
        if typ == "Chimpanzee":
            arr_ch.append(i)

    if arr_gb:
        arr_gb = srt(arr_gb)
    else:
        arr_gb = {}
    if arr_gor:
        arr_gor = srt(arr_gor)
    else:
        arr_gor = {}
    if arr_or:
        arr_or = srt(arr_or)
    else:
        arr_or = {}
    if arr_ch:
        arr_ch = srt(arr_ch)
    else:
        arr_ch = {}

    return {
        "Gorilla": arr_gor.get("name"),
        "Gibbon": arr_gb.get("name"),
        "Orangutan": arr_or.get("name"),
        "Chimpanzee": arr_ch.get("name"),
    }
