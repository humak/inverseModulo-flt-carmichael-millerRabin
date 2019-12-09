#udl computational tools for problem solving lab3
#humakal
#'19
import math 
import random

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return x, gcd

def modulo_inverse(a, m):
    x, gcd = egcd(a, m)
    if (gcd != 1):    
        return -1
    else:   
        i = (x % m + m) % m
    return i


def isPrime(n): 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
  
def fermats_little_theo(n,a):
    if(isPrime(n) == True and a%n != 0):
        print("Fermat's little theorem works.")
        return pow(a, n-1)%n
    else:                    #for pseudo prime numbers like 124.  124,5->1 but 124,3->27
        if (pow(a, n-1)%n == 1): 
            print("Pseudo Prime!!")
            return pow(a, n-1)%n
        else:
            print("None!!")
            return pow(a, n-1)%n

def carmichael_numbers(n):
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            if pow(i, n-1, n) != 1:
                return -1
    return 1
        
        


def miller_rabin(n):
    a = random.randint(2,n-1)  
    if(n == 2):
        return True
    if(n%2 == 0):
        #not prime
        return False
    else:
        x = n-1
        s=0
        while(x%2 == 0):
            x = x/2
            s = s+1
        d = (n-1)/pow(2, s)
    r = 0
    while( pow(a,d)%n != 1 and (pow(a, pow(2,r)*d) +1 )% n !=0 and r <= s-1):
        r = r+1
    if(r == s-1):
        return False
    else:
        return True


def main():
   
    print(modulo_inverse(1973, 103)) #ii) #58
    print(modulo_inverse(103, 1973)) #ii) #862
    
    print(fermats_little_theo(17, 2) ) 
    print(fermats_little_theo(124, 3)) 
    print(fermats_little_theo(124, 5)) 
    print(fermats_little_theo(561, 2)) 

    print("Carmichael numbers")
    for i in range (10000):
        if (carmichael_numbers(i) == 1):    
            #print(i)  #too much number, enable to print.
            continue

    print(miller_rabin(41))


if __name__== "__main__":
  main()


