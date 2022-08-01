
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
def mergeSort(arr, n):
    pass

arr = insertionSort(arr, n)
print(arr)