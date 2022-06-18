def beautifulTriplets(d, arr):
    # Write your code here
    count = 0
    n = len(arr)
    for i in range(n-2):
        found = False
        for j in range(i+1,n-1):
            if ((arr[j] - arr[i]) == d):
                for k in range(j+1,n):
                    if ((arr[k] - arr[j]) == d):
                        count = count + 1
                        found = True
                        break
                    
            if found == True:
                break
    return count
