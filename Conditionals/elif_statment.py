age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
elif age >= 16:
    print("You are eligible to drive")
elif age ==0:
    print("you are  born yet")
else:
    print("You are not eligible to vote or drive")
    # space is important in python, indentation is used to define the scope of the code block