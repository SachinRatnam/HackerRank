def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    l = len(arr)
    # Write your code here
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
            
    print('{0:.6f}'.format(pos / l)) 
    print('{0:.6f}'.format(neg / l))
    print('{0:.6f}'.format(zero / l))
