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
