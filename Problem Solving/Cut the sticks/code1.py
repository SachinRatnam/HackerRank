def cutTheSticks(arr):
    ls = []
    while len(arr) >= 1:
        ls.append(len(arr))
        minn = min(arr)
        arr = [i-minn for i in arr if i!=minn]
    return ls
