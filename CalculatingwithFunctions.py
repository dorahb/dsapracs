def zero(b = None): #your code here
    if b is None:
        return 0
    else:
        return b(0)
def one(b=None): #your code here
    if b is None:
        return 1
    else:
        return b(1)
            
            
def two(b=None): #your code here
    if b is None:
        return 2
    else:
        return b(2)
def three(b=None): #your code here
    if b is None:
        return 3
    else:
        return b(3)
def four(b=None): #your code here
    if b is None:
        return 4
    else:
        return b(4)
def five(b=None): #your code here
    if b is None:
        return 5
    else:
        return b(5)
def six(b=None): #your code here
    if b is None:
        return 6
    else:
        return b(6)
def seven(b=None): #your code here
    if b is None:
        return 7
    else:
        return b(7)
def eight(b=None): #your code here
    if b is None:
        return 8
    else:
        return b(8)
def nine(b=None): #your code here
    if b is None:
        return 9
    else:
        return b(9)

def plus(number): #your code here
    return lambda x: x + number
    
def minus(number): #your code here
    return lambda x: x - number
def times(number): #your code here
    return lambda x : x * number
def divided_by(number): #your code here
    return lambda x : x // number