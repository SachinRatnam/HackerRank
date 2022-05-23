def viralAdvertising(n):
    # Write your code here
    share = 5
    l = 0
    total_like = 0
    for i in range(n):
        like_per_day = share//2
        total_like = total_like + like_per_day
        share = like_per_day * 3
    return total_like
