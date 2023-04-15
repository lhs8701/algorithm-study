def solution(price):

    if price >= 500000:
        return price * 80 // 100
    elif price >= 300000:
        return price  * 90 // 100
    elif price >= 100000:
        return price * 95 // 100

    return price