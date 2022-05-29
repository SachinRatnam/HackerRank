def extraLongFactorials(n):
    # Write your code here
    fac = 1
    if n == 0:
        print(0)
    while n > 0:
        fac = fac * n
        n = n-1
    print(fac)
