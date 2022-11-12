def median(a,b):
    if len(a)>len(b):
        a,b=b,a
    lo = 0 
    hi = len(a)
    tl = len(a)+len(b)
    
   # a---> a0 , a1 |, a3 , a4 , a5
   #               |---------|                  segregation  a2<=b4  and b4<=a3 thats valid segregation
   # b---> b0 , b1 , b2 , b3 | b4 , b5 , b6 , b7 
                                                  
    
    while lo <= hi:
        m = (lo + hi) //2
        bl= (tl+1)//2 - m
        a2 = a[m-1] if m!=0 else -10**8
        a3 = a[m] if m!=len(a) else 10**8
        b3 = b[bl-1] if bl!=0 else -10**8
        b4 = b[bl] if bl!=len(b) else 10**8
        if a2 <= b4 and b3<=a3:
            if tl%2==0:
                lm = max(b3,a2)
                rm = min(a3,b4)
                return (lm + rm)/2.0
            else:
                lm = max(b3,a2)
                return lm
        elif a2 > b4 :
            hi = m -1
        else:
            lo = m+1
    return -1
a = [100000]
b=[100001]
print(median(a,b))
        
