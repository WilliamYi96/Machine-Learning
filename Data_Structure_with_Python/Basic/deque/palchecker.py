from pythonds.basic.deque import Deque 

def palchecker(aString):
    d = Deque()

    for ch in aString:
        d.addRear(ch)

    sideEqual = True
    # print(sideEqual, d.size())

    while sideEqual and d.size() > 1:
        first = d.removeFront()
        last = d.removeRear()
        # print(first)
        if first != last: 
            sideEqual = False  
    
    return sideEqual

print(palchecker('abcdcba'))
print(palchecker("adbsdfdsf"))