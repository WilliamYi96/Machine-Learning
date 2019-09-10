# ParChecker, created by Kai Yi on 09/09/2019

from pythonds.basic.stack import Stack 

def parChecker(symbolString):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('(((()))')) # False
print(parChecker('((()))')) # True