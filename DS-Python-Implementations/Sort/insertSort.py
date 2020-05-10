def insertionSort(aList):
    for i in range(1, len(aList)):
        value = aList[i]
        pointer = i

        while pointer > 0 and aList[pointer-1]>value:
            aList[pointer] = aList[pointer-1]
            pointer = pointer - 1

        aList[pointer] = value

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

# Continue from PG133