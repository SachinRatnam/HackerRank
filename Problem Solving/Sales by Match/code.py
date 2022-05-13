def sockMerchant(n, ar):
    # Write your code here
    d1 = {}
    for i in ar:
        if i in d1:
            d1[i] = d1[i] + 1
        else:
            d1[i] = 1
     
    pair = 0
    for j in list(d1.values()):
        pair = pair + j//2
    return pair
