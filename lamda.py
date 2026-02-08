square = lambda x: x ** 2 # this is a lambda function that takes one parameter 'x' and returns the square of 'x'
print(square(5)) # this will call the 'square' lambda function with the argument 5 and print the returned value, which is 25
cube = lambda x: x ** 3 # this is a lambda function that takes one parameter 'x' and returns the cube of 'x'
print(cube(3)) # this will call the 'cube' lambda function with the argument 3 and print the returned value, which is 27
add = lambda a, b: a + b # this is a lambda function that takes two parameters 'a' and 'b' and returns the sum of 'a' and 'b'
print(add(2, 3)) # this will call the 'add' lambda function with the arguments 2 and 3 and print the returned value, which is 5
multiply = lambda x, y: x * y # this is a lambda function that takes two parameters 'x' and 'y' and returns the product of 'x' and 'y'
print(multiply(4, 5)) # this will call the 'multiply' lambda function with the arguments 4 and 5 and print the returned value, which is 20
average = lambda a, b, c: (a + b + c) / 3 # this is a lambda function that takes three parameters 'a', 'b', and 'c' and returns the average of 'a', 'b', and 'c'
print(average(10, 20, 30)) # this will call the 'average' lambda function with the arguments 10, 20, and 30 and print the returned value, which is 20.0
max_value = lambda a, b: a if a > b else b # this is a lambda function that takes two parameters 'a' and 'b' and returns the maximum of 'a' and 'b'
print(max_value(5, 10)) # this will call the 'max_value' lambda function with the arguments 5 and 10 and print the returned value, which is 10
min_value = lambda a, b: a if a < b else b # this is a lambda function that takes two parameters 'a' and 'b' and returns the minimum of 'a' and 'b'
print(min_value(5, 10)) # this will call the 'min_value' lambda function with the arguments 5 and 10 and print the returned value, which is 5
is_even = lambda x: x % 2 == 0 # this is a lambda function that takes one parameter 'x' and returns True if 'x' is even, otherwise it returns False
print(is_even(4)) # this will call the 'is_even' lambda function with the argument 4 and print the returned value, which is True
print(is_even(5)) # this will call the 'is_even' lambda function with the argument 5 and print the returned value, which is False
is_odd = lambda x: x % 2 != 0 # this is a lambda function that takes one parameter 'x' and returns True if 'x' is odd, otherwise it returns False
print(is_odd(4)) # this will call the 'is_odd' lambda function with the argument 4 and print the returned value, which is False
print(is_odd(5)) # this will call the 'is_odd' lambda function with the argument 5 and print the returned value, which is True
is_positive = lambda x: x > 0 # this is a lambda function that takes one parameter 'x' and returns True if 'x' is positive, otherwise it returns False
print(is_positive(5)) # this will call the 'is_positive' lambda function with the argument 5 and print the returned value, which is True
print(is_positive(-3)) # this will call the 'is_positive' lambda function with the argument -3 and print the returned value, which is False
is_negative = lambda x: x < 0 # this is a lambda function that takes one parameter 'x' and returns True if 'x' is negative, otherwise it returns False
print(is_negative(5)) # this will call the 'is_negative' lambda function with the argument 5 and print the returned value, which is False
print(is_negative(-3)) # this will call the 'is_negative' lambda function with the argument -3 and print the returned value, which is True
is_palindrome = lambda s: s == s[::-1] # this is a lambda function that takes one parameter 's' and returns True if 's' is a palindrome (reads the same forwards and backwards), otherwise it returns False
print(is_palindrome("racecar")) # this will call the 'is_palindrome' lambda function with the argument "racecar" and print the returned value, which is True
print(is_palindrome("hello")) # this will call the 'is_palindrome' lambda function with the argument "hello" and print the returned value, which is False
is_vowel = lambda c: c.lower() in 'aeiou' # this is a lambda function that takes one parameter 'c' and returns True if 'c' is a vowel (a, e, i, o, u), otherwise it returns False
print(is_vowel('a')) # this will call the 'is_vowel' lambda function with the argument 'a' and print the returned value, which is True
print(is_vowel('b')) # this will call the 'is_vowel' lambda function with the argument 'b' and print the returned value, which is False
print(is_vowel('E')) # this will call the 'is_vowel' lambda function with the argument 'E' and print the returned value, which is True (since the function converts the character to lowercase before checking)
is_consonant = lambda c: c.lower() in 'bcdfghjklmnpqrstvwxyz' # this is a lambda function that takes one parameter 'c' and returns True if 'c' is a consonant (any letter that is not a vowel), otherwise it returns False
print(is_consonant('a')) # this will call the 'is_consonant' lambda function with the argument 'a' and print the returned value, which is False
print(is_consonant('b')) # this will call the 'is_consonant' lambda function with the argument 'b' and print the returned value, which is True


