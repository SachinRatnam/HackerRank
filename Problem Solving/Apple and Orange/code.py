def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    a_d = [a+ap for ap in apples]
    o_d = [b+orng for orng in oranges]
    no_app = 0
    no_orng = 0
    for i in a_d:
        if s<= i <= t:
            no_app += 1
    
    for j in o_d:
        if s<= j <= t:
            no_orng += 1
    
    print(no_app)
    print(no_orng)
