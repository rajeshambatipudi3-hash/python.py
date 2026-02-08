# cSpell:ignore gramming progr mming programm nges appl grap ples ananas applesorangesbananasgrapes
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
print(name.isdigit()) # this will print True if all characters in the string are digits, which is False
print(name.isalnum()) # this will print True if all characters in the string are alphanumeric (letters and numbers), which is False (since there is a space character)
print(name.isupper()) # this will print True if all characters in the string are uppercase, which is False
print(name.islower()) # this will print True if all characters in the string are lowercase, which is True   
print(name.strip()) # this will print the string with any leading or trailing whitespace removed, which is 'hello world' (since there is no whitespace  to remove)
print(name.lstrip()) # this will print the string with any leading whitespace removed, which is 'hello world' (since there is no leading whitespace to remove)
print(name.rstrip()) # this will print the string with any trailing whitespace removed, which is 'hello world' (since there is no trailing whitespace to remove)

text = "python programming is fun" # this will create a string variable named text with the value "python programming is fun"
print(text.find("programming")) # this will print the index of the first occurrence of the substring "programming" in the string text, which is 7
print(text.find("Python")) # this will print -1 since the substring "Python" (with an uppercase "P") is not found in the string text (which contains "python" with a lowercase "p")
print(text.find("is")) # this will print the index of the first occurrence of the substring "is" in the string text, which is 18
print(text.find("fun")) # this will print the index of the first occurrence of the substring "fun" in the string text, which is 21
print(text.find("java")) # this will print -1 since the substring "java" is not found in the string text
print(text.find(" ")) # this will print the index of the first occurrence of the space character in the string text, which is 6
print(text.find("p")) # this will print the index of the first occurrence of the character  "p" in the string text, which is 0
print(text.find("g")) # this will print the index of the first occurrence of the character "g" in the string text, which is 10
print(text.find("z")) # this will print -1 since the character "z" is not found in the string text      
print(text.replace("python", "java")) # this will print the string with all occurrences of "python" replaced with "java", which is 'java programming is fun'
print(text.replace(" ", "_")) # this will print the string with all occurrences of the space    character replaced with "_", which is 'python_programming_is_fun'
print(text.replace("is", "was")) # this will print the string with all occurrences of "is" replaced with "was", which is 'python programming was fun'
print(text.replace("fun", "awesome")) # this will print the string with all occurrences of "fun" replaced with "awesome", which is 'python programming is awesome'
print(text.replace("programming", "coding")) # this will print the string with all occurrences of "programming" replaced with "coding", which is 'python coding is fun'
print(text.replace("o", "0")) # this will print the string with all occurrences of "o" replaced with "0", which is 'pyth0n pr0gramming is fun'
print(text.replace("a", "4")) # this will print the string with all occurrences of "a" replaced with "4", which is 'python progr4mming is fun'
print(text.replace("e", "3")) # this will print the string with all occurrences of      "e" replaced with "3", which is 'python programming is fun' (since there are no occurrences of "e" in the string text)
print(text.replace("i", "1")) # this will print the string with all occurrences of "i" replaced with "1", which is 'python programm1ng 1s fun'
print(text.replace("s", "5")) # this will print the string with all occurrences of "s" replaced with "5", which is 'python programming i5 fun'      


text = "apples, oranges, bananas, grapes" # this will create a string variable named text with the value "apples, oranges, bananas, grapes"
print(text.split(", ")) # this will print a list of the substrings in the string text that are separated by the substring ", ", which is ['apples', 'oranges', 'bananas', 'grapes']
print(text.split("a")) # this will print a list of the substrings in the string text that are separated by the character "a", which is ['apples, or', 'nges, b', 'n', 'n', 's, gr', 'pes']
print(text.split(" ")) # this will print a list of the substrings in the string text that are separated by the space character, which is ['apples,', 'oranges,', 'bananas,', 'grapes']
print(text.split(",")) # this will print a list of the substrings in the string text that are separated by the comma character, which is ['apples', ' oranges', ' bananas', ' grapes']
print(text.split("e")) # this will print a list of the substrings in the string text that are separated by the character "e", which is ['appl', 's, orang', 's, bananas, grap', 's']
print(text.split("p")) # this will print a list of the substrings in the string text that are separated by the character "p", which is ['a', 'ples, oranges, bananas, gra', 'es']
print(text.split("s")) # this will print a list of the substrings in the string text that are separated by the character "s", which is ['apple', ', orange', ', banana', ', grape', '']
print(text.split("n")) # this will print a list of the substrings in the string text that are separated by the character "n", which is ['apples, oranges, ba', 'a', 'as, grapes']
print(text.split("g")) # this will print a list of the substrings in the string text that are separated by the character "g", which is ['apples, oran', 'es, bananas, ', 'rapes']
print(text.split("o")) # this will print a list of the substrings in the string text that are separated by the character "o", which is ['apples, ', 'ranges, bananas, grapes']
print(text.split("a, ")) # this will print a list of the substrings in the string text that are separated by the substring "a, ", which is ['apples', 'oranges', 'bananas, grapes']
print(text.split(", a")) # this will print a list of the substrings in the string text that are separated by the substring ", a", which is ['apples', 'oranges', 'bananas, grapes']
print(text.split(", o")) # this will print a list of the substrings in the string text that are separated by the substring ", o", which is ['apples', 'ranges, bananas, grapes']
print(text.split(", b")) # this will print a list of the substrings in the string text that are separated by the substring ", b", which is ['apples, oranges', 'ananas, grapes']
print(text.split(", g")) # this will print a list of the substrings in the string text that are separated by the substring ", g", which is ['apples, oranges, bananas', 'rapes']
print(text.split(", gr")) # this will print a list of the substrings in the string text that are separated by the substring ", gr", which is ['apples, oranges, bananas', 'apes']
print(text.split(", gr")) # this will print a list of the substrings in the string text that are separated by the substring ", gr", which is ['apples, oranges, bananas', 'apes']   


text = "apples, oranges, bananas, grapes" # this will create a string variable named text with the value "apples, oranges, bananas, grapes  "
print(text.strip()) # this will print the string with any leading or trailing whitespace removed, which is 'apples, oranges, bananas, grapes' (since there is no leading or trailing whitespace to remove)
print(",".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with the separator ",", which is 'apples,oranges,bananas,grapes'
print(" ".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with the separator " ", which is 'apples oranges bananas grapes'
print("-".join(['apples', 'oranges', 'bananas', 'grapes '])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes '] with the separator "-", which is 'apples-oranges-bananas-grapes '
print("".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with no separator, which is 'applesorangesbananasgrapes'
print(" and ".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with the separator " and ", which is 'apples and oranges and bananas and grapes'
print(", ".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with the separator ", ", which is 'apples, oranges, bananas, grapes'
print("; ".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with the separator "; ", which is 'apples; oranges; bananas; grapes'
print(" | ".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with the separator " | ", which is 'apples | oranges | bananas | grapes'  
print("".join(['apples', 'oranges', 'bananas', 'grapes'])) # this will print the string that is created by joining the elements of the list ['apples', 'oranges', 'bananas', 'grapes'] with no separator, which is 'applesorangesbananasgrapes' 
