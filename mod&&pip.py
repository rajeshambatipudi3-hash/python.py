import math

print(math.sqrt(16)) # this will print 4.0
print(math.pow(2, 3)) # this will print 8.0 
print(math.pi) # this will print 3.141592653589793
print(math.e) # this will print 2.718281828459045
print(math.sin(math.pi / 2)) # this will print 1.0
print(math.cos(0)) # this will print 1.0    
print(math.tan(math.pi / 4)) # this will print 1.0
print(math.log(100, 10)) # this will print 2.0
print(math.factorial(5)) # this will print 120
print(math.gcd(48, 18)) # this will print 6
print(math.lcm(12, 15)) # this will print 60
print(math.ceil(2.3)) # this will print 3
print(math.floor(2.7)) # this will print 2
print(math.fabs(-5)) # this will print 5.0
print(math.isqrt(16)) # this will print 4


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
