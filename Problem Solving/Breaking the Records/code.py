def breakingRecords(scores):
    # Write your code here
    best = None
    least = None
    break_most = 0
    break_least = 0
    for score in scores:
        if best == None:
            best = score
            least = score
        elif(score > best):
            best = score
            break_most += 1
        elif(score < least):
            least = score
            break_least += 1
    return [break_most,break_least]
