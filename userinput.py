a = input("Enter a value: ") # this will take user input as a string
print(a) # this will print the user input
b = input("enter your age :")
age = int(b) # this will convert the string input to an integer
print(b)
if age > 18: # this will check if the age is greater than 18
	print("ur adult") # this will print if the age is greater than 18
elif age == 0: # this will check if the age is equal to 0
	print("ur not born yet") # this will print if the age is equal to 0
elif age < 18: # this will check if the age is less than 18
	print("ur not adult") # this will print if the age is less than 18
	print("wait for 18 :") # this will print if the age is less than 18
