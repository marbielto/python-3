#SoloLearn
#returning from functions
#functions as objects
"""
def max(x,y):
    if x >= y:
        return x
    else:
        return y
print(max(4, 7))
z = max(8,5)
print(z)
"""
'''
def shortest_string(x, y):
    if len(x) <= len(y):
        return x
    else:
        return y
print(shortest_string("Amor", "Dor"))
'''
"""
def add_numbers(x, y ):
    total = x + y
    return total
    print("this won't be printed")
    
print(add_numbers(4, 5))
"""
"""
def multiply(x, y):
	return x * y 

a = 4
b = 7
operation = multiply
print(operation(a, b))
"""

def add(x, y):
	return x + y

def do_twice(func, x, y):
	return func(func(x,y), func(x,y))

a = 5 
b = 10

print(do_twice(add, a, b))
