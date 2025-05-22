a =int(input("Enter a number:"))
match a:
    case 1:
        print("a is 1")
    case 12:
        print("a is 12")
    case 32:
        print("a is 32")
    case 4:
        print("a is 4")
    case _:
        print("a is not 1, 12, 32 or 4")
# The match statement is used to compare a value against a series of patterns