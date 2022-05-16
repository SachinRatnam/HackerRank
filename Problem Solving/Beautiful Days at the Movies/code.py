def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for x in range(i,j+1):
        st1 = str(x)
        st2 = st1[::-1]
        it = int(st2)
        div = abs(x-it)/k
        
        
        if int(div) == div:
            count += 1
    return count
