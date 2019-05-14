
#Show what excemptions can do.
#Dev: Eric Timm (I feel a little awkward calling myself a dev)
#5/13/2019

#declaring values
a=5
b=5

# Creating a while loop which should error out without an exception handler... we are forcing a number to be divided by zero.
while(b > -3): # the divisor, is positive and will reduce by a value of one until -3 
    try: #exception syntax which tells Python to try this operation a/b and print the output.
        print(a/b)
        b=b-1 # This reduces the value of b after it loops once
    except ZeroDivisionError: # this is exception handling, wihtout this the script would terminate and we couldn't get negative values.
        print("you cannot divide by zero")
        b=b-1
    finally: 
        print('finally')