from collections import Counter
prime = [1]*(10**6+2)
upto = 10**6+2
prime[0]=prime[1] = 0
lcf = [0]*(10**6+2)
for i in range(2,upto):
    if prime[i]:
        for j in range(2*i,upto,i):
            prime[j] = 0
            if lcf[j]==0:
                lcf[j] = i


def getFaxx(num):
    pf = Counter()
    if prime[num]:
        pf[num] +=1
    else:
        while num!=1:
            if lcf[num] == 0:
                div = num
            else:
                div = lcf[num]
            pf[div]+=1
            num//=div
    return pf