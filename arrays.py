
# Maximum difference between two elements such that larger element appears after the smaller number

def max_diff(arr, n):

    m_diff = arr[1] - arr[0]
    min_ele = arr[0]

    for i in range(1, n):

        if arr[i] - min_ele > m_diff:
            m_diff = arr[i] - min_ele

        if arr[i] < min_ele:
            min_ele = arr[i]

    return m_diff

# Find the subarray with least average

def leastAvg(arr, n, k):

    if n < k:
        return -1

    curr_sum = sum(arr[:k]);
    min_sum = curr_sum;

    for i in range(k, n):
        curr_sum = curr_sum - arr[i - k] + arr[i];
        if curr_sum < min_sum:
            min_sum = curr_sum;

    return min_sum;


def findSplitPoint(arr, n) :

    leftSum = 0
    for i in range(0, n) :
        leftSum += arr[i]

    rightSum = 0
    for i in range(n-1, -1, -1) :

        rightSum += arr[i]

        leftSum -= arr[i] 
   
        if (rightSum == leftSum) :
            return i 

    return -1



t = int(input())

for _ in range(t):

    n = int(input())
    s = input()

    d = dict(Counter(s))
    flag = 0

    for key, val in d.items():

        if val % 2:
            flag = 1
            break 

    if flag:
        print("NO")
    else:
        print("YES")
        
consonants = list("bcdfghjklmnpqrstvwxyz")

for _ in range(t):

    n = int(input())
    s = input()

    if n < 4:
        print("YES")

    elif n == 4:

        if (s[0] in consonants) and (s[1] in consonants) and (s[2] in consonants) and (s[3] in consonants):
            print("NO")

        else:
            print("YES")

    else:

        flag = 0

        for i in range(n - 4):

            if (s[i] in consonants) and (s[i + 1] in consonants) and (s[i + 2] in consonants) and (s[i + 3] in consonants):
                flag = 1
                break

        if flag:
            print("NO")

        else:
            print("YES")