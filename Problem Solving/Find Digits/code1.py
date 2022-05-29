def findDigits(n):
    temp = str(n)
    count = 0
    for x in temp:
        try:
            if n % int(x) == 0:
                count += 1
        except ZeroDivisionError:
            pass
    
    return count
