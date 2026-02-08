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
print(name.split(" ")) # this will print a list of the substrings in the string that    are separated by the character " ", which is ['hello', 'world']
print(name.find("o")) # this will print the index of the first occurrence of the character "o" in the string, which is 4
print(name.count("o")) # this will print the number of occurrences of the character "o" in the string, which is 2
print(name.startswith("h")) # this will print True if the string starts with "h", which is True
print(name.endswith("d")) # this will print True if the string ends with "d", which is True
print(name.isalpha()) # this will print True if all characters in the string are alphabetic, which is False (since there is a space character)
print(name.isdigit()) # this will print True if all characters in the string are digits, which is False
print(name.isalnum()) # this will print True if all characters in the string are alphanumeric (letters and numbers), which is False (since there is a space character)
print(name.isupper()) # this will print True if all characters in the string are uppercase, which is False
print(name.islower()) # this will print True if all characters in the string are lowercase, which is True
print(name.isspace()) # this will print True if all characters in the string are whitespace, which is False (since there are non-whitespace characters in the string)
print(name.index("o")) # this will print the index of the first occurrence of the character "o" in the string, which is 4
print(name.rindex("o")) # this will print the index of the last occurrence of the character "o" in the string, which is 7
print(name.startswith("h")) # this will print True if the string starts with "h", which is True
print(name.endswith("d")) # this will print True if the string ends with "d", which is True
print(name.isalpha()) # this will print True if all characters in the string are alphabetic