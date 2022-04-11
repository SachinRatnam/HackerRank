def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    mx = sum(arr[0:4])
    mn = sum(arr[1:])
    print('{} {}'.format(mx,mn))
