def kaprekarNumbers(p, q):
    # Write your code here
    k = []
    
    for i in range(p,q+1):
        len_i = len(str(i))
        square = str(i ** 2)
        r_part = square[-len_i:]
        l_part = square[:-len_i] or '0'
        
        new_no = int(r_part) + int(l_part)
        if (i == new_no):
            k.append(new_no)
    if k:
        print(*k)
    else:        
        print('INVALID RANGE')
