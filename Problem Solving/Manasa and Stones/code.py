def stones(n, a, b):
    # Write your code here
    s1 = set()
    for i in range(n):
        stone = a*i + b*(n-1-i)
        s1.add(stone)
    return sorted(s1)
