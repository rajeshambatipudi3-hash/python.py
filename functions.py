# functions example
def greet(name): # this is a function definition that takes one parameter called 'name'
    return f"Hello, {name}!"    # this is the body of the function that returns a greeting message using an f-string to include the value of the 'name' parameter

print(greet("World"))  # this will call the 'greet' function with the argument "World" and print the returned greeting message, which is "Hello, World!"
print(greet("Alice"))  # this will call the 'greet' function with the argument "Alice" and print the returned greeting message, which is "Hello, Alice!"
print(greet("Bob"))    # this will call the 'greet' function with the argument "Bob" and print the returned greeting message, which is "Hello, Bob!"    
print(greet("Charlie")) # this will call the 'greet' function with the argument "Charlie" and print the returned greeting message, which is "Hello, Charlie!"   
def add(a, b): # this is a function definition that takes two parameters called 'a' and 'b'
    return a + b # this is the body of the function that returns the sum of 'a' and 'b' 
print(add(2, 3)) # this will call the 'add' function with the arguments 2 and 3 and print the returned sum, which is 5
print(add(10, 20)) # this will call the 'add' function with the arguments 10 and 20 and print the returned sum, which is 30
print(add(-5, 5)) # this will call the 'add' function with the arguments -5 and 5 and print the returned sum, which is 0
print(add(3.5, 2.5)) # this will call the 'add' function with the arguments 3.5 and 2.5 and print the returned sum, which is 6.0    
def multiply(x, y): # this is a function definition that takes two parameters called 'x' and 'y'
    return x * y # this is the body of the function that returns the product of 'x' and 'y' 
print(multiply(2, 3)) # this will call the 'multiply' function with the arguments 2 and 3 and print the returned product, which is 6    
print(multiply(10, 20)) # this will call the 'multiply' function with the arguments 10 and 20 and print the returned product, which is 200
print(multiply(-5, 5)) # this will call the 'multiply' function with the arguments -5 and 5 and print the returned product, which is -25
print(multiply(3.5, 2.5)) # this will call the 'multiply' function with the arguments 3.5 and 2.5 and print the returned product, which is 8.75 

