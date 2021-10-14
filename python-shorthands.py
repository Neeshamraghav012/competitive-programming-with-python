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
a = 6.7798
print("{0:2f}".format(a))

# round(ans, 6) -> ans = input, 6 -> number of digits to be rounded.

########## 2D Matrix + Arrays ###############################################################################
arr = list(map(int, input().splitI()))
Matrix = [[0 for in range(n)] for j in range(m)]

########### Prefix and Suffix Sum ################################################################################

pref = [sum(test_list[ : i + 1]) for i in range(len(test_list))]
test_list = [3, 4, 1, 7, 9, 1]

test_list.reverse()
suff = [sum(test_list[ : i + 1 ]) for i in range(len(test_list))]


###### MAPS AND (HASING) ########################################################################################
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
    
for i in L:
    d[i] += 1


###### GroupBy Make groups of consecutive similar elements(e.g. 11001 -> 1:2, 0:2, 1:1)  #######################
key_func = lambda x: x[0]
for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))


###### SubStrings #################### Total Substrings = n * (n + 1) / 2 #######################################
sub = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2)]

if __name__ == "__main__" :

	print("Hello World!")

"""

    Contributed By Neesham


"""