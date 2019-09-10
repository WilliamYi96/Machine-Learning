# bubbleSort created by Kai Yi on 09/09/2019

def bubbleSort(aList):
    for i in range(len(aList)-1, 0, -1):
        for j in range(i):
            if aList[j+1] < aList[j]:
                aList[j+1], aList[j] = aList[j], aList[j+1]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)