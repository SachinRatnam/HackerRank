def squares(a, b):
    # Write your code here
    sq_rt_a = math.ceil(a ** 0.5)
    sq_rt_b = math.floor(b ** 0.5)
    
    return sq_rt_b - sq_rt_a + 1
  
# 1 is added for ----  how many natural numbers are there in [5..9] ? with 5 and 9 inclusion
#                       Max-Min+1 or 9-5+1 = 5 for [5, 6, 7, 8, 9]
