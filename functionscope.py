def sum(a, b):
    return a + b
print(sum(2, 3)) # this will call the 'sum' function with the arguments 2 and 3 and print the returned value, which is 5
print(sum(10, 20)) # this will call the 'sum' function with the arguments 10 and 20 and print the returned value, which is 30
print(sum(-5, 5)) # this will call the 'sum' function with the arguments -5 and 5 and print the returned value, which is 0
print(sum(3.5, 2.5)) # this will call the 'sum' function with the arguments 3.5 and 2.5 and print the returned value, which is 6.0  
print(sum("Hello, ", "World!")) # this will call the 'sum' function with the arguments "Hello, " and "World!" and print the returned value, which is "Hello, World!" (string concatenation works with the '+' operator in Python when both operands are strings)
print(sum([1, 2], [3, 4])) # this will call the 'sum' function with the arguments [1, 2] and [3, 4] and print the returned value, which is [1, 2, 3, 4] (list concatenation works with the '+' operator in Python when both operands are lists)
print(sum((1, 2), (3, 4))) # this will call the 'sum' function with the arguments (1, 2) and (3, 4) and print the returned value, which is (1, 2, 3, 4) (tuple concatenation works with the '+' operator in Python when both operands are tuples)

z = 10 # this will assign the value 10 to the variable 'z'
print(z) # this will print the value of 'z', which is 10
def outer_function(): # this is a function definition for 'outer_function' which takes no parameters
   
    def sum(a, b): # this is a nested function definition for 'sum' which takes two parameters 'a' and 'b'
        c = a + b # this will calculate the sum of 'a' and 'b' and assign it to the variable 'c'    

        return c # this will return the value of 'c' from the 'sum' function
    result = sum(5, 10) # this will call the nested 'sum' function with the arguments 5 and 10 and assign the returned value, which is 15, to the variable 'result'
    print(result) # this will print the value of 'result', which is 15  



# local variable example
def local_variable_example():
    x = 10 # this is a local variable 'x' that is defined inside the function 'local_variable_example'
    print(x) # this will print the value of 'x', which is 10
local_variable_example() # this will call the 'local_variable_example' function and print the value of 'x', which is 10
# print(x) # this will raise a NameError because 'x' is a local variable and is not accessible outside the function 'local_variable_example'    
print(z) # this will print the value of 'z', which is 10 (since 'z' is a global variable and is accessible throughout the entire program)

# global variable example
y = 20 # this is a global variable 'y'
def global_variable_example():
    print(y) # this will print the value of 'y', which is 20
global_variable_example()

# modifying global variable inside function
count = 0 # global variable
def increment():
    global count # declare that we want to use the global variable
    count += 1
    print(count)
increment() # prints 1
increment() # prints 2
print(count) # prints 2

# docstring example
def add(a, b): # this is a function definition for 'add' which takes two parameters 'a' and 'b'
    """Returns the sum of two numbers."""
    return a + b # this is the body of the function that returns the sum of 'a' and 'b'
print(add(2, 3)) # this will call the 'add' function with the arguments 2 and 3 and print the returned value, which is 5

def multiply(x, y): # this is a function definition for 'multiply' which takes two parameters 'x' and 'y'   
    
    """
        y: Second number
    
    Returns: # this is a docstring that describes the parameters and return value of the 'multiply' function    

        The product of x and y
    """
    return x * y # this is the body of the function that returns the product of 'x' and 'y'
print(multiply(4, 5)) # this will call the 'multiply' function with the arguments 4 and 5 and print the returned value, which is 20 


print(add.__doc__) # this will print the docstring of the 'add' function, which is "Returns the sum of two numbers."    

print(multiply.__doc__) # this will print the docstring of the 'multiply' function, which is:

