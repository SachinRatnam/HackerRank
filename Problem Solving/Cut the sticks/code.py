def cutTheSticks(arr):
    # Write your code here
    x = 0
    final_list = []
    while (x == 0):
        final_list.append(len(arr))
        string = []
        mn = min(arr)
        for num in arr:
            if (num != mn):
                string.append(num - mn)
            else:
                continue
        arr = string[:]
        
        if (len(arr)== 0):
            x = 1
    return final_list
