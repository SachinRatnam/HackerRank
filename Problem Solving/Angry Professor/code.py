def angryProfessor(k, a):
    # Write your code here
    count = 0
    for i in range(len(a)):
        if a[i] <= 0:
            count += 1
        if count >= k:
            return 'NO'
    return 'YES'
