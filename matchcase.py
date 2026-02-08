a = 10

match a:
    case 0:
        print("a is zero") # this will print if a is equal to 0
    case 10:
        print("a is ten") # this will print if a is equal to 10
    case 20:
        print("a is twenty") # this will print if a is equal to 20  
    case 30:
        print("a is thirty") # this will print if a is equal to 30
    case _:
        print("a is something else") # this will print if a is not equal to 0 or 10, which means a is something else

a = int(input("Enter a value for a: ")) # this will take user input for a and convert it to an integer
match a:
    case 0:
        print("you won a car") # this will print if a is equal to 0
    case 1:
        print("you won a bike") # this will print if a is equal to 1
    case 2:
        print("you won a phone") # this will print if a is equal to 2
    case 3:
        print("you won a laptop") # this will print if a is equal to 3
    case 4:
        print("you won a tablet") # this will print if a is equal to 4