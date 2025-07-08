# to check in string  digit upppercase lowercase 
import random
s = "Hello123"
is_digit = 0
is_upper = 0
is_lower = 0
for char in s:
   if char.isdigit():
      is_digit += 1

##randomixation
x =[1, 2, 3, 4, 5]
print("Original list:", str(x))
random.shuffle(x)
print("Shuffled list:", str(x))

x =['anant', 'baba', 'coco']
print("Original list:", str(x))
random.shuffle(x)       
print("suffled list:",str(x))

   


       