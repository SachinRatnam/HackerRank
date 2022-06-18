def beautifulTriplets(d, arr):
    # Write your code here
    n = len(arr)
    triplet = 0
    for i in range(n):
        if arr[i]+d in arr and arr[i] + 2*d in arr:
            triplet += 1
    return triplet
