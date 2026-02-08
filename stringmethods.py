name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting) # this will print "Hello, Alice!"   
name = "Alice"
a =len(name) # this will calculate the length of the string "Alice", which is 5
print(a) # this will print the value of a, which is 5

name = "hello world"
print(name.upper()) # this will print the string in uppercase, which is 'HELLO WORLD'
print(name.lower()) # this will print the string in lowercase, which is 'hello world'       
print(name.capitalize()) # this will print the string with the first character capitalized and the rest in lowercase, which is 'Hello world'
print(name.title()) # this will print the string with the first character of each word capitalized, which is 'Hello World'
print(name.strip()) # this will print the string with any leading or trailing whitespace removed, which is 'hello world' (since there is no whitespace)
print(name.replace("o", "0")) # this will print the string with all occurrences of "o" replaced with "0", which is 'hell0 w0rld'
print(name.split(" ")) # this will print a list of the substrings in the string that