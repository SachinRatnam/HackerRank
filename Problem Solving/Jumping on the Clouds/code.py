def jumpingOnClouds(c):
    # Write your code here
    cloud = 0
    jump = 0
    while cloud < len(c)-2:
        jump += 1
        if c[cloud+2] == 1:
            cloud = cloud + 1
        else:
            cloud = cloud + 2
            
    if cloud == len(c)-2:
        jump = jump + 1
    
    return jump
