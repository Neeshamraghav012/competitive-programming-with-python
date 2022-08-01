
n = int(input())
arr = list(map(int, input().split()))

ans, cnt = [], 0

# Bubble Sort
def bubbleSort(arr, n):

    for i in range(n):
        # n - i - 1
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr;

# Selection Sort
def selectionSort(arr, n):

    for i in range(n):

        m_ele = arr[i]
        m_ind = i 

        for j in range(i + 1, n):

            if arr[j] < arr[i]:
                m_ele = arr[j]
                m_ind = j 

        arr[i], arr[m_ind] = arr[m_ind], arr[i]

    return arr;

# Insertion Sort
def insertionSort(arr, n):

    for i in range(1, n):
        for j in range(i):

            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i] 

    return arr;

# Merge Sort
c = [0] * 4
def mergeSort(arr, n):
    
    if len(arr) <= 1:
        return 0

    mid = n // 2 

    l = arr[:mid]
    r = arr[mid:]

    mergeSort(l, len(l))
    mergeSort(r, len(r))

    i, j, k = 0, 0, 0 

    while (i < len(l) and j < len(r)):

        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1 

        else:
            arr[k] = r[j]
            j += 1

        k += 1

    while (i < len(l)):
        arr[k] = l[i]
        k += 1 
        i += 1

    while (j < len(r)):
        arr[k] = r[j]
        k += 1
        j += 1

    return arr;

arr = mergeSort(arr, n)
print(arr)