def serviceLane(width, cases):
    # Write your code here
    arr = [min(width[ i[0]:i[1]+1 ]) for i in cases]
        # print( min(width[i[0]:i[1]]) )
    return arr
