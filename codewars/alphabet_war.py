# https://www.codewars.com/kata/5938f5b606c3033f4700015a/
def alphabet_war(fight):
    SCORE = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
        'm': -4,
        'q': -3,
        'd': -2,
        'z': -1,
    }
    arr = []
    next_item = True
    before_item = True
    for v in fight:
        if v in SCORE and next_item:
            arr.append(SCORE[v])
            before_item = True
        elif v in SCORE:
            next_item = True
        elif v == '*':
            if arr and next_item and before_item:
                arr.pop()
                before_item = False
            next_item = False
        else:
            arr.append(0)
            next_item = True
    c = sum(arr)
    if c > 0:
        return('Left side wins!')
    elif c < 0:
        return('Right side wins!')
    else:
        return("Let's fight again!")
