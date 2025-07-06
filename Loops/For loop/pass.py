# 🟡 What is pass statement in Python?
# 🔸 pass is a null statement.

#     It means: "Do nothing"

#     It’s used when a statement is required syntactically, but you don’t want to write any code there (for now).

# ✅ Why use pass?

#     🔹 To create empty functions, loops, classes, etc.

#     🔹 Useful during code development or debugging.

#     🔹 Prevents syntax errors when Python expects code but you haven’t written it yet.

class Student:
    pass

def hello():
    pass  # function is not implemented yet



x = 10
if x > 5:
    pass  # maybe you’ll write logic later
else:
    print("x is 5 or less")

