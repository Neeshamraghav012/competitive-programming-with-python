
# Recursive Python program to check
# if a string is subsequence
# of another string

def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False
 
    # If last characters of two
    # strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)

    """
    for counting number of subsequences
    if (a[m - 1] == b[n - 1])
        return count(a, b, m - 1, n - 1) +
               count(a, b, m - 1, n)

    """
 
    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)


def countSubsequence(s, n):
    cntG = 0
    cntF = 0
    result = 0
    C=0
 
 
    # Traversing the given string
    for i in range(n):
        if (s[i] == 'G'):
             
            # If the character is 'G', increment
            # the count of 'G', increase the result
            # and update the array.
            cntG += 1
            result += C
            continue
 
        # If the character is 'F', increment
        # the count of 'F' and update the array.
        if (s[i] == 'F'):
            cntF += 1
            C += cntG
            continue
 
        # Ignore other character.
        else:
            continue
     
    print(result)

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
 
    # Create a temp string with value str1.str1
    temp = string1 + string1
 
    # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of
    # the second string in temp
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

s = "geeks"
temp = s + s
n = len(s)
print(s)

for i in range(1, n + 1):
    print(temp[i : i + n])