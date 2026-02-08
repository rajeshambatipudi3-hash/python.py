for i in range(0, 11): # this will loop from 0 to 10
    if i == 5: # this will check if the current value of i is equal to 5
        break # this will exit the loop if i is equal to 5
    print(i) # this will print the current value of i in each iteration of the loop, which will be 0, 1, 2, 3, and 4

for i in range(0, 20): # this will loop from 0 to 19
    if i == 10: # this will check if the current value of i is equal to 10
        continue # this will skip the rest of the loop and move to the next iteration if i is equal to 10
    print(i) # this will print the current value of i in each iteration of the loop, which will be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18 and 19 (10will be skipped)

    print("Loop ended") # this will print "Loop ended" after the loop has finished executing    

    print(i) # this will print the current value of i in each iteration of the loop, which will be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18 and 19 (10 will be skipped)
    if i == 10: # this will check if the current value of i is equal to 10
        pass # this will do nothing and continue to the next iteration of the loop if i is equal to 10
    
print("Loop ended") # this will print "Loop ended" after the loop has finished executing

print(i) # this will print the final value of i after the loop has finished executing, which will be 19 since the loop ends when i reaches 20 and the last value of i that is printed is 19
if i == 19: # this will check if the final value of i is equal to 19
    pass # this will do nothing since i is equal to 19 , so it will simply pass and continue with the rest of the code
