def sockMerchant(n, ar):
    # Write your code here
    A = set(ar)
    pairs = 0
    
    for element in A:
        pairs += ar.count(element) // 2
    return pairs
