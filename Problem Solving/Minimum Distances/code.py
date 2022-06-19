def minimumDistances(a):
    # Write your code here
    l = len(a)
    arr = []
    for i in range(l):
        if a[i] in a[i+1:]:
            x = a.index(a[i],i+1,l)
            d = abs(i-x)
            arr.append(d)
    
    if(len(arr) > 0):
        return min(arr)
    else:
        return -1
