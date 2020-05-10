# if sorted, then return.

def shortBubbleSort(aList):
    exchange = True
    length = len(aList) - 1
    while length > 0 and exchange:
        exchange = False
        for i in range(length):
            if aList[i+1] < aList[i]:
                exchange = True
                aList[i], aList[i+1] = aList[i+1], aList[i]
        length = length - 1

alist = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(alist)
print(alist)