number = int(input("Enter a number: "))

sum =0;
temp = number
while temp>0:
    digit =  temp%10# Get the last digit
    sum = sum + digit**3 # Add the cube of the digit to the sum
    temp = temp//10 # Remove the last digit
if sum == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")