def permutationEquation(p):
    # Write your code here
    y = []
    p.insert(0,0)
    for i in range(1,len(p)):
        ind = p.index(p.index(i))
        y.append(ind)
    return y
