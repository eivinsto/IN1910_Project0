"Function to add two numbers"
def add(x,y):
    return x+y

"Function to calculate factorial of number"
def factorial(x):
    sum = 1
    #Looping over all numbers from 1 to x, multiplying them with each other
    for i in range(1,x+1):
        sum *= i
    return sum

"Function to calculate sine of number, using the truncated Taylor expansion"
def sin(x,N):
    sum = 0
    #Looping from i=0 to N, adding the terms of the Taylor expansion to the sum
    for i in range(N+1):
        sum += ( (-1)**i * x**(2*i + 1) )/factorial(2*i + 1)
    return sum


"Function to divide first number by the second"
def divide(x,y):
    return x/y

"Function to calculate cosine of number, using the truncated Taylor expansion"
def cos(x,N):
    sum = 0
    #Looping from i=0 to N, adding the terms of the Taylor expansion to the sum
    for i in range(N+1):
        sum += ( (-1)**i * x**(2*i) ) /factorial(2*i)
    return sum 

"Function to calculate the first number to the power of the second"
def power(x,y):
    return x**y
