# parsChecker created by Kai Yi on 09/09/2019

from pythonds.basic.stack import Stack

def parsChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while balanced and index < len(symbolString):
        symbol = symbolString[index]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = '{[('
    closes = '}])'
    return opens.index(open) == closes.index(close)

print(parsChecker('{{{{]]}')) # False
print(parsChecker('(){[]}')) # True