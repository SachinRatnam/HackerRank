def jumpingOnClouds(c, k):
    e=100
    pos=0
    n=len(c)
    while True:
        pos=(pos+k)%n
        if c[pos]==1:
            e-=3
        else:
            e-=1
        
        if pos==0:
            break
    return e
