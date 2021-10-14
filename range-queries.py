from math import sqrt, ceil, floor, gcd, log2
from sys import stdin, stdout
from collections import Counter, defaultdict, OrderedDict, deque
from itertools import combinations, groupby
from heapq import heappop, heappush, heapify

d = defaultdict(int)
    
L = [1, 2, 3, 4, 2, 4, 1, 2]
    
###### first element of a dict ###########################################################
res = next(iter(test_dict))
for i in L:
    d[i] += 1

key_func = lambda x: x[0]
  
for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))

### Segmented Tree (0- based index) [l, r) ######
N = 100000;
 
# Max size of tree
tree = [0] * (2 * N);
 
# function to build the tree
def build(arr) :
 
    # insert leaf nodes in tree
    for i in range(n) :
        tree[n + i] = arr[i];
     
    # build the tree by calculating parents
    for i in range(n - 1, 0, -1) :
        tree[i] = tree[i << 1] + tree[i << 1 | 1];
 
# function to update a tree node
def updateTreeNode(p, value) :
     
    # set value at position p
    tree[p + n] = value;
    p = p + n;
     
    # move upward and update parents
    i = p;
     
    while i > 1 :
         
        tree[i >> 1] = tree[i] + tree[i ^ 1];
        i >>= 1;
 
# function to get sum on interval [l, r)
def query(l, r) :
 
    res = 0;
     
    # loop to find the sum in the range
    l += n;
    r += n;
     
    while l < r :
     
        if (l & 1) :
            res += tree[l];
            l += 1
     
        if (r & 1) :
            r -= 1;
            res += tree[r];
             
        l >>= 1;
        r >>= 1
     
    return res;


# Binary indexed Tree (1 based) give sum to ith index.
def getsum(BITTree,i):
    s = 0 #initialize result
 
    # index in BITree[] is 1 more than the index in arr[]
    i = i+1
 
    # Traverse ancestors of BITree[index]
    while i > 0:
 
        # Add current element of BITree to sum
        s += BITTree[i]
 
        # Move index to parent node in getSum View
        i -= i & (-i)
    return s
 
# Updates a node in Binary Index Tree (BITree) at given index
# in BITree. The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITTree , n , i ,v):
 
    # index in BITree[] is 1 more than the index in arr[]
    i += 1
 
    # Traverse all ancestors and add 'val'
    while i <= n:
 
        # Add 'val' to current node of BI Tree
        BITTree[i] += v
 
        # Update index to that of parent in update View
        i += i & (-i)
 
 
# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
 
    # Create and initialize BITree[] as 0
    BITTree = [0]*(n+1)
 
    # Store the actual values in BITree[] using update()
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
 
    # Uncomment below lines to see contents of BITree[]
    #for i in range(1,n+1):
    #     print BITTree[i],
    return BITTree
 
 
#### Range Update#####

# Updates such that getElement() gets an increased
# value when queried from l to r.
def update(BITree, l, r, n, val):
      
    # Increase value at 'l' by 'val'
    updateBIT(BITree, n, l, val)
  
    # Decrease value at 'r+1' by 'val'
    updateBIT(BITree, n, r+1, -val)
 
# Driver Code
if __name__ == "__main__" :
 
    n, q = map(int, input().split())

    a = list(map(int, input().split()))

    build(a);
     

    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

    BITTree = construct(freq,len(freq))

    print(getsum(BITTree,5))

    updatebit(BITTree, len(freq), 3, 6)

    print(getsum(BITTree,5))

    print(query(1, 3));
     

    updateTreeNode(2, 1);

    print(query(1, 3));
     

######### Square root decomposition #############################################################

s = [1, 2, -3, 2, 3, 4, -6, 1, 2, 3, 4, 5, -8, 5, 6, 3]

n = len(s)

block_size = int(sqrt(n)) + 1

def constructblock(a, n):

    block_size = int(sqrt(n)) + 1

    block = [0] * (block_size)

    for i in range(n):

        block[i//block_size] += a[i]

    return block

######################## 0 based index ####################################
def squarRootQuery(l, r, block, block_size, a, n):

    i = l
    s = 0
    while i <= r:

        if (i % block_size and i + block_size - 1 <= r):

            s += block[i//block_size]
            i += block_size

        else:
            s += a[i]
            i += 1

    return s