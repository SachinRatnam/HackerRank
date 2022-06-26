def countingValleys(steps, path):
    # Write your code here
    count = 0
    valley = 0
    for i in path:
        if(count == 0 and i == 'D'):
            valley += 1
        
        if i == 'U':
            count += 1
        elif i == 'D':
            count -= 1
        
    return valley
