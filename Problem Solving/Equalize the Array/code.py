def equalizeArray(arr):
    # Write your code here
    d1 = {}
    for i in arr:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    l1 = list(d1.values())
    s1 = sum(l1)-max(l1)
    return s1
