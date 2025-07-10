n= int(input("Enter a number: "))

dis={x:x**2 for x in range(1, n+1)}  # Dictionary comprehension to create a dictionary with squares
print("The square of each number from 1 to", n, "is:", dis)  # Output: The square of each number from 1 to n is: {1: 1, 2: 4, ..., n: n^2}