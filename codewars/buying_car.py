# https://www.codewars.com/kata/554a44516729e4d80b000012
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    if startPriceOld >= startPriceNew:
        return [0, startPriceOld - startPriceNew]
    k = percentLossByMonth / 100
    n = 0
    c = 1
    while (startPriceOld + n) < startPriceNew:
        startPriceOld = startPriceOld * (1 - k)
        startPriceNew = startPriceNew * (1 - k)
        n += savingperMonth
        c += 1
        if c % 2 == 0:
            k += 0.005

    return [c - 1, round(startPriceOld + n - startPriceNew)]
