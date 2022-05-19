def getMoneySpent(keyboards, drives, b):
    # Write your code here
    if min(keyboards) + min(drives) > b:
        return -1
    else:
        y = 0
        for i in keyboards:
            for j in drives:
                s = i + j
                if s <= b and s > y:
                    y = s
        return y
