try:
    a =int(input("Enter the number:"))
    b = int(input("Enter the second number :"))

    print("what kind of operation due you want to perform.\n Press + for additon \n Press - for subtraction \n Press / for division \n press * for multiplication")

    o = input("Enter the operation:")
    match o:
        case "+":
            print(f"The result of{a} and {b} is {a+b}")

        case "-":
            print(f"The result of {a} and {b} is {a-b}")

        case "*":
            print(f"The result of {a} and {b} is {a*b}")

        case "/":
            print(f"The result of {a} and {b} is {a/b}")

        case _:
            print("YOU ENTER WRONG OPERATION")



except Exception as e:
    print("Enter a valid value of a and b")
