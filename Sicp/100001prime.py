from math import sqrt, floor
def isPrime(n):
    if n=1:
        return false
    elif n<4:
        return true
    elif  n%2==0:
        return false
    elif n<9:
        return true
    elif n%3=0:
        return false
    else:
        r=floor( sqrt(n) )
        f=5
        while f<=r
        if n% f=0:
            return false
            break
        if n%(f+2)=0:
            return false
            break
        f=f+6
        
        return true (in all other cases)
