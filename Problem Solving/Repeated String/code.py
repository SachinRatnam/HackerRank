def repeatedString(s, n):
    # Write your code here
    rep = n // len(s)
    count_s = s.count('a')
    count_total = rep * count_s

    count_part = 0
    s_part = n % len(s) 
    if (s_part != 0):
        count_part = s[:s_part].count('a')
    return count_total + count_part
