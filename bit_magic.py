

import math
 
def highestPowerof2(n):
 
    p = int(math.log(n, 2));
    return int(pow(2, p));
 
def smallestPowerof2(n):

    p = math.ceil(math.log(n, 2))
    return int(pow(2, n))


def countSetBits(n):
 
    count = 0
    while (n):
        n &= (n-1)
        count+= 1
     
    return count

## AND(A, B) <= min(A, B)

arr = [1, 2, 3, 4, 5]

## 48 >> 3 (48 / 2 ^ 3) => (48 / 8), x >> k => x / 2^k

## 1 << 3 (2 ^ 3) => (8), x << k => x * 2^k

bit_pos = [0] * 32

for i in range(31):

    for j in range(5):

        if (arr[j] & (1 << i)):

            bit_pos[i] += 1


x = 4
"""
for i in range(31, -1, -1):

    if (x & (1 << i)):
        print(1)

    else:
        print(0)
"""

# Utility function to check number of
# elements having set msb as of pattern
def checkBit(pattern,arr,  n) :
    count = 0
     
    for i in range(0, n) :
        if ((pattern & arr[i]) == pattern) :
            count = count + 1
    return count
 
# Function for finding maximum and
# value pair
def maxAND (arr,  n) :
    res = 0
     
    # iterate over total of 32bits
    # from msb to lsb
    for bit in range(31,-1,-1) :
       
        # find the count of element
        # having set  msb
        count = checkBit(res | (1 << bit), arr, n)
  
        # if count >= 2 set particular
        # bit in result
        if ( count >= 2 ) :
            res =res | (1 << bit)
             
    return res
     
  
# Driver function
arr = [4, 8, 6, 2]
n = len(arr)
print("Maximum AND Value = ", maxAND(arr, n))