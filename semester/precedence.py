# print(3<<4<<2)# Output: 48
# print(3<<4>>2) # Output: 12
# print(3>>4<<2) # Output: 0


# from datetime import datetime
# first_date = datetime(2023, 10, 1)
# second_date = datetime(2023, 10, 31)
# date_difference = second_date - first_date
# print("Difference in days:", date_difference.days)  # Output: Difference in days:



list1 = ['audi', 'video', 'image', 'text', 'audio']
result ='^'.join(list1)
print(type(result))
print("Concatenated string:", result)  # Output: Concatenated string: audivideoimagetextaudio