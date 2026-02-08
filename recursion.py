# recursion example: calculating the factorial of a number
def factorial(n): # this is a function definition that takes one parameter called 'n'
    if n == 0: # this is the base case of the recursion, where if 'n' is 0, the function returns 1
        return 1
    else: # this is the recursive case, where the function calls itself with 'n-1' and multiplies it by 'n'
        return n * factorial(n - 1)     
print(factorial(5)) # this will call the 'factorial' function with the argument 5 and print the returned value, which is 120
print(factorial(0)) # this will call the 'factorial' function with the argument 0 and print the returned value, which is 1
print(factorial(1)) # this will call the 'factorial' function with the argument 1 and print the returned value, which is 1
print(factorial(10)) # this will call the 'factorial' function with the argument 10 and print the returned value, which is 3628800  
print(factorial(20)) # this will call the 'factorial' function with the argument 20 and print the returned value, which is 2432902008176640000  
print(factorial(100)) # this will call the 'factorial' function with the argument 100 and print the returned value, which is 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000 
print(factorial(170)) # this will call the 'factorial' function with the argument 170 and print the returned value, which is 7.257415615307998e+306 (since the result exceeds the maximum value for integers in Python, it is returned as a floating-point number in scientific notation)   
print(factorial(171)) # this will call the 'factorial' function with the argument 171 and print the returned value, which is inf (infinity) since the result exceeds the maximum value for floating-point numbers in Python)    
