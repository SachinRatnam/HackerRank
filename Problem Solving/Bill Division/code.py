def bonAppetit(bill, k, b):
    # Write your code here
    actual_bill = int((sum(bill)-bill[k]) / 2) 
    if (b == actual_bill):
        print('Bon Appetit')
    else:
       print(b - actual_bill)
