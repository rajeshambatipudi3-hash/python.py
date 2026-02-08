template = "Hello, {}. You are {} years old."
name = "Alice"
age = 30
print(template.format(name, age)) # this will print "Hello, Alice. You are 30 years old."   
template = "Hello, {0}. You are {1} years old. {0}, have a nice day!"
print(template.format(name, age)) # this will print "Hello, Alice. You are 30 years old. Alice, have a nice day!"
template = "Hello, {name}. You are {age} years old."    
print(template.format(name=name, age=age)) # this will print "Hello, Alice. You are 30 years old."
template = "Hello, {0}. You are {age} years old."   