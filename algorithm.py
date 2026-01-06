# 최솟값 기준 오름차순
def selectionSort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

# 최댓값 기준 오름차순
def selectionSort(list):
    for i in range(len(list)-1, -1, -1):
        max_idx = i
        for j in range(i-1, -1, -1):
            if list[j] > list[max_idx]:
                max_idx = j
        list[i], list[max_idx] = list[max_idx], list[i]

# 최댓값 오름차순
def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

# 최솟값 오름차순
def bubbleSort(list):
    for i in range(len(list)-1, -1, -1):
        for j in range(len(list)-1, len(list)-1-i, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]

# 오름차순
def insertionSort(list):
    for i in range(1, len(list)):
        tmp = list[i]
        j = i-1
        while j >= 0 and list[j] > tmp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = tmp


# 맨 오른쪽 pivot 선택, 오름차순 정렬
def partition(list, low, high):
    i = low - 1
    pivot = list[high]

    for j in range(low, high):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]
    return(i+1)



# 맨 왼쪽 pivot, 내림차순
def partition(list, low, high):
    i = low
    pivot = list[low]

    for j in range(low+1, high+1):
        if list[j] > pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i], list[low] = list[low], list[i]
    return(i)


#################################################################################


# DFS
adj_list = []
n = len(adj_list)
visited = [False for _ in range(n)]

def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)


# BFS
def bfs(v):
    queue = []
    visited[v] = True
    queue.append(v)

    while len(queue) != 0:
        u = queue.pop(0)
        for w in adj_list[u]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)


#################################################################################

# quickSort
def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)


# K-selection
def Kselection(a, low, high, k):
    pivot = partition(a, low, high)
    if k < pivot:
        return Kselection(a, low, pivot-1, k)
    elif k == pivot:
        return a[k]
    else:
        return Kselection(a, pivot+1, high, k)