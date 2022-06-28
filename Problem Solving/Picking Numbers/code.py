def pickingNumbers(a):
    # Write your code here
    mx = 0
    for i in a:
        c1 = a.count(i)
        c2 = a.count(i-1)
        f1 = c1 + c2 
        if f1 > mx:
            mx = f1
    return mx
