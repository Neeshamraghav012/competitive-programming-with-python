from math import sqrt, ceil, floor, gcd, log2
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, OrderedDict, deque
from itertools import combinations, groupby
from time import time
from heapq import heappop, heappush, heapify


mod = 1000000007
INT_MAX = sys.maxsize;
######## precision ##########################################################################################

# round(ans, 6) -> ans = input, 6 -> number of digits to be rounded.

########## 2D Matrix #########################################################################################

Matrix = [[0 for in range(n)] for j in range(m)]

########### Prefix and Suffix ################################################################################

pref = [sum(test_list[ : i + 1]) for i in range(len(test_list))]
test_list = [3, 4, 1, 7, 9, 1]

test_list.reverse()
suff = [sum(test_list[ : i + 1 ]) for i in range(len(test_list))]

###### Fibbonacci Sequence Variables #########################################################################
MAX = 10**6
f = [0] * MAX

###### MAP ####################################################################################################
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
    
for i in L:
    d[i] += 1


###### GroupBy #################################################################################################
key_func = lambda x: x[0]
for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))


###### SubStrings #################### Total Sub = n * (n + 1) / 2 ##############################################
sub = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2)]
   

###### Excecution Time ########################################################################################## 
""""
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

t0 = time()
factorial(10**5)
print('Elapsed time :', time() - t0 )
"""

def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(sqrt(n)) + 1))

####### Eular Totioent Function (all the primes form (1 -> n)) ####################################################
def phi(n) :
 
    result = n  
    p = 2
    while p * p<= n :

        if n % p == 0 :

            while n % p == 0 :
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
         
  
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n)))
  
    return int(result)


###### Mod Inverse ################################################################################################
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):

        q = a // m
 
        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0
 
    return x


###### Fast Modular Exponentiation ########################################################################
def fastmod(a, b):

    ans = 1
    global mod

    a = a % mod

    if(a==0):

        return 0

    while(b):

        if(b & 1):

            ans=(ans*a)%mod

        b = b>>1

        a = (a*a)%mod


    return ans%mod

###### Little Fermat Theorem (used to find modular inverse if a and m are comprime) #########################
def fermat(a):
    global mod
    return fastmod(a,mod-2) % mod


######## A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square ######
######## Returns n'th fibonacci number using table f[] #########################################################
def fib(n) :
    # Base cases
    if (n == 0) :
        return 0
    if (n == 1 or n == 2) :
        f[n] = 1
        return (f[n])
 
    # If fib(n) is already computed
    if (f[n]) :
        return f[n]
 
    if( n & 1) :
        k = (n + 1) // 2
    else :
        k = n // 2
 
    # Applying above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if((n & 1) ) :
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
    else :
        f[n] = (2*fib(k-1) + fib(k))*fib(k)
 
    return f[n]


######### Factorial of a large Number #############################################################################
def multiply(x, res, res_size):

    carry = 0

    for i in range(res_size):

        prod = res[i] * i + carry

        res[i] = prod % 10

        carry = prod // 10

    while (carry):

        res[res_size] = carry % 10

        carry = carry // 10
        res_size = res_size + 1
         
    return res_size


def fact(n):

    res = [0] * 500

    res[0] = 1

    res_size = 1

    for i in range(2, n):

        multiply(i, res, res_size)

    print ("Factorial of given number is")
    i = res_size-1
    while i >= 0 :
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i = i - 1



######## Sieve #####################################################################################################
def sieveOfEratosthenes(N):

    prime = [1 for i in range(N + 1)]	
    p  = 2	
    while (p * p <= N):

    	    
        if (prime[p] == 1):
    	        
    	    for i in range(p * p, N + 1, p):
    	        prime[i] = 0
    	                 
        p += 1  	
    	
    a = []
    for i in range(2, N + 1):
    	    
    	if (prime[i] == 1):
    	        
    	    a.append(i)	        
        
    return a

"""
x = sieveOfEratosthenes(10)
for i in x:
    print(x)
"""

######## Prime Factors of N ########################################################################################
def primeFactors(n):
    
    res = []
    for i in range(2, int(sqrt(n)) + 1):
        
        if (n % i) == 0:
            res.append(i)
            
        while (n % i) == 0:
            
            n //= i 
            
    if n > 2: 
        res.append(n)
        
    return res


########### Prime Factors of a number using preprocessing ##########################################################
spf = [0] * MAXN

def sieve():
    spf[1] = 1
    for i in range(2, MAXN):

        spf[i] = i
 

    for i in range(4, MAXN, 2):
        spf[i] = 2
 
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
         

        if (spf[i] == i):

            for j in range(i * i, MAXN, i):

                if (spf[j] == j):
                    spf[j] = i

sieve()
def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
 
    return ret


############## Function to print the number  O(n) solution #####################################################################
def catalan(n):
     
    cat = 1
 
    # For the first number
    print(cat, " ", end = '')# C(0)
 
    # Iterate till N
    for i in range(1, n):
         
        # Calculate the number
        # and print it
        cat *= (4 * i - 2);
        cat //= (i + 1);
        print(cat, " ", end = '')



"""
s = sys.stdin.readline()

n = int(sys.stdin.readline())

sys.stdount.write(str(n))
"""
divisors = [0] * N

def findTotalDivisors():

    divisors[0] = divisors[1] = divisors[2] = divisors[3] = 0 ;

    for i in range(2, N + 1):

        for j in range(2, (N // i) + 1):

            divisors[i*j] += 1;

#findTotalDivisors()

if __name__ == "__main__" :

	catalan(5)