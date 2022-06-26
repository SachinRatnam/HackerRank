def migratoryBirds(arr):
    # Write your code here
    x= list(set(arr))
    y = [0] * (max(x)+1)
     
    for i in x:
        y[i] = arr.count(i)
    return y.index(max(y))
