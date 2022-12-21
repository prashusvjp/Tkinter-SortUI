
#Ascending bubble sort
def bubbleSortAsc(array):
    swapped = False
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    return array

#Descending bubble sort
def bubbleSortDsc(array):
    swapped = False
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]<array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    return array

#Ascending selection sort
def selectionSotAsc(array):
    for i in range(len(array)-1):
        minIndex = i
        for idx in range(i + 1, len(array)-1):
            if array[idx] < array[minIndex]:
                minIndex = idx
        array[i], array[minIndex] = array[minIndex], array[i]
    return array

#Descending selection sort
def selectionSortDsc(array):
    for i in range(len(array)-1):
        maxIndex = i
        for idx in range(i + 1, len(array)-1):
            if array[idx] > array[maxIndex]:
                maxIndex = idx
        array[i], array[maxIndex] = array[maxIndex], array[i]
    return array

#Insertion Sort
def insertionSortAsc(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

def insertionSortDsc(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] < key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

#Merge Sort
def mergeSortAsc(nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = mergeSortAsc(nums[:mid+1])
    lst2 = mergeSortAsc(nums[mid+1:])
    result = mergeAsc(lst1, lst2)
    return result

def mergeAsc(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst

def mergeSortDsc(nums):
    if len(nums)==1:
        return nums
    mid = (len(nums)-1) // 2
    lst1 = mergeSortDsc(nums[:mid+1])
    lst2 = mergeSortDsc(nums[mid+1:])
    result = mergeDsc(lst1, lst2)
    return result

def mergeDsc(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
        if lst1[i]>lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    if i>len(lst1)-1:
        while(j<=len(lst2)-1):
            lst.append(lst2[j])
            j+=1
    else:
        while(i<=len(lst1)-1):
            lst.append(lst1[i])
            i+=1
    return lst




#Quick Sort
def quickSortAsc(array):
    if len(array)> 1:
        pivot=array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSortAsc(smlr_lst) + equal_lst + quickSortAsc(grtr_lst))
    else:
        return array

def quickSortDsc(array):
    if len(array)> 1:
        pivot=array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSortDsc(grtr_lst) + equal_lst + quickSortDsc(smlr_lst))
    else:
        return array