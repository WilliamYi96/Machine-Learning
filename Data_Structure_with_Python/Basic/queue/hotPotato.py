# HotPotato Problem

from pythonds.basic.queue import Queue 

def hotPotato(nameList, num):
    q = Queue()
    for name in nameList:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))