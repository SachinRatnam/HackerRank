def taumBday(b, w, bc, wc, z):
    # Write your code here
    if (bc > (wc + z)):
        return ( (b+w) * wc ) + (b * z)  
    elif (wc > (bc + z)):
        return ( (b+w) * bc ) + (w * z) 
    else:
        return (b * bc) + (w * wc)
