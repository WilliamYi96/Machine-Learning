from pythonds.basic.stack import Stack 

def divideBy2(decimal):
    s = Stack()

    while decimal > 0:
        number = decimal % 2
        s.push(number)
        decimal = decimal // 2

    final = ""
    while not s.isEmpty():
        final += str(s.pop())

    return final

print(divideBy2(15))
print(divideBy2(8))
