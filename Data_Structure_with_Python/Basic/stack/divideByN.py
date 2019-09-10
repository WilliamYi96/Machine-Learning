# 10 to N (2-16)

from pythonds.basic.stack import Stack 

def divideByN(decimal, base):
    
    digits = "0123456789ABCDEF"
    s = Stack()

    while decimal > 0:
        number = decimal % base
        s.push(number)
        decimal = decimal // base
    
    final = ''
    while not s.isEmpty():
        final += digits[s.pop()]  
    
    return final

print(divideByN(25, 2))
print(divideByN(25, 16))

# Continue from PG45 of Python Data Structure
        