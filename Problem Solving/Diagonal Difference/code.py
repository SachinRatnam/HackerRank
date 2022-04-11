def diagonalDifference(arr):
    length = len(arr)
    l_to_r = [arr[i][i] for i in range(length)]            # traversing 2 D matrix left to right
    sum_left = sum(l_to_r)                                    
    r_to_l = [arr[i][length-i-1] for i in range(length)]    # traversing 2 D matrix right to left
    sum_rit = sum(r_to_l) 
    
    return abs(sum_left - sum_rit)
