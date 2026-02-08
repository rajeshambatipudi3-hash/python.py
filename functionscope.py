def sum(a, b):
    return a + b
print(sum(2, 3)) # this will call the 'sum' function with the arguments 2 and 3 and print the returned value, which is 5
print(sum(10, 20)) # this will call the 'sum' function with the arguments 10 and 20 and print the returned value, which is 30
print(sum(-5, 5)) # this will call the 'sum' function with the arguments -5 and 5 and print the returned value, which is 0
print(sum(3.5, 2.5)) # this will call the 'sum' function with the arguments 3.5 and 2.5 and print the returned value, which is 6.0  
print(sum("Hello, ", "World!")) # this will call the 'sum' function with the arguments "Hello, " and "World!" and print the returned value, which is "Hello, World!" (string concatenation  works with the '+' operator in Python when both operands are strings    print(sum([1, 2], [3, 4])) # this will call the 'sum' function with the arguments [1, 2] and [3, 4] and print the returned value, which is [1, 2, 3, 4] (list concatenation works with the '+' operator in Python when both operands are lists )
print(sum((1, 2), (3, 4))) # this will call the 'sum' function with the arguments (1, 2) and (3, 4) and print the returned value, which is (1, 2, 3, 4) (tuple concatenation works with the '+' operator in Python when both operands are tuples    )

z = 10 # this will assign the value 10 to the variable 'z'
print(z) # this will print the value of 'z', which is 10
def outer_function(): # this is a function definition for 'outer_function' which takes no parameters