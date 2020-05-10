def selectionSort(aList):
    for i in range(len(aList)-1, 0, -1):
        mmax = 0
        for j in range(1, i+1):
            if aList[mmax] < aList[j]:
                mmax = j
        aList[i], aList[mmax] = aList[mmax], aList[i]

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)