x =20# This is a global variable
def anat():
    global x  # Declare x as global to modify it
    print("x is value",x)
    x=10
    print("x is value",x)

anat()

print("x is value",x)