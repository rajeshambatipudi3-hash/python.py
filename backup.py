# ========== BACKUP FILE - ALL PYTHON CODE ==========

# ========== test.py ==========
a = 23 # this is an integer
b = "43" # this is a string
c = 123
print(int(b)) # this will convert the string "43" to an integer 43
print(str(a)) # this will convert the integer 23 to a string "23"
c = str(b)
print(type(c)) # this will print <class 'str'> since c is now a string  

user_input = input("Enter a number: ")
print(f"You entered: {user_input} (type: {type(user_input).__name__})")
num = int(user_input)
print(f"Converted to integer: {num} (type: {type(num).__name__})")

# ========== userinput.py ==========
print("how are \n u") # this will print "how are" and "u" on a new line
print("how are \t u") # this will print "how are" and "u" with a tab space in between

# ========== matchcase.py ==========
a = 10
match a:
    case 0:
        print("a is zero")
    case 10:
        print("a is ten")
    case 20:
        print("a is twenty")
    case 30:
        print("a is thirty")
    case _:
        print("a is something else")

a = int(input("Enter a value for a: "))
match a:
    case 0:
        print("you won a car")
    case 1:
        print("you won a bike")
    case 2:
        print("you won a phone")
    case 3:
        print("you won a laptop")
    case 4:
        print("you won a tablet")

# ========== loops.py ==========
i = 1
while i <= 10:
    print(f"5 X {i} = {5 * i}")
    i += 1

# ========== functions.py ==========
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

def add(a, b):
    return a + b
print(add(2, 3))

def multiply(x, y):
    return x * y
print(multiply(2, 3))

# ========== lamda.py ==========
square = lambda x: x ** 2
print(square(5))

cube = lambda x: x ** 3
print(cube(3))

add = lambda a, b: a + b
print(add(2, 3))

multiply = lambda x, y: x * y
print(multiply(4, 5))

# ========== mod&&pip.py ==========
import math
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.pi)

# pip install requests
import requests
response = requests.get('https://api.github.com')
print(response.status_code)

# pip install numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))

# pip install pandas
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)

# pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig('plot.png')
