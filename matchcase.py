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
