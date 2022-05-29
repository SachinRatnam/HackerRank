def findDigits(n):
    # Write your code here
    l1 = [int(i) for i in str(n)]
    div = 0
    
    for j in l1:
        if j == 0:
            continue
        elif n % j == 0:
            div += 1
    return div
