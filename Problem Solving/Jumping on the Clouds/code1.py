def jumpingOnClouds(c):
    i = count_jumps = 0
    length = len(c)

    while i < length - 1:
        if i < length - 2 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        count_jumps += 1

    return count_jumps
