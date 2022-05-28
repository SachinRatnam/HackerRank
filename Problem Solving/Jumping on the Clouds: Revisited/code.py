def jumpingOnClouds(c, k):
    e = 100 #initial energy
    n = len(c)
    i = k % n #initial jump from 0
    e -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        e -= c[i] * 2 + 1
    
    return e
