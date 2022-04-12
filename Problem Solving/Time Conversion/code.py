def timeConversion(s):
    # Write your code here
    if s == '12:00:00AM' :
        return '00:00:00'
    elif s == '12:00:00PM':
        return '12:00:00'
    elif 'AM' in s:
        return s[:8]
    elif 'PM' in s:
        x = int(s[:2])+ 12 
        return str(x) + s[2:8]
