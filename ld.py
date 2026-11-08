#  list

# A list stores multiple items in order.	
# A list is created using square brackets [].	
# List items are accessed by index.	
# List items can be duplicated.	
# Example: a = [10, 20, 30]	

# a = [10, 20, 30]
# print(a[0])


# Dictionary
# A dictionary stores data as key-value pairs
# A dictionary is created using curly braces {}
# Values are accessed by keys
# Keys must be unique
# Example: a = {"name": "Riad", "age": 20}





import pyautogui
import time

n = int(input("number"))

time.sleep(5)

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)

    pyautogui.write(spaces + stars)
    pyautogui.press("enter")
