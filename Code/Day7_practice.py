# Day 7, 17 June 2025 Python Practice
**Comment**
# is my hastag for brain, Python ignores it but my brain loves it!

print("Comments are fun")

# This part prints a welcome message

print("Welcome to my program")

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
  print("err")
except ValueError: 
    print("invalid input")

# 1. Juice Squeezer 🍊 (Handle wrong input)

try:
    fruits = int(input("How many oranges do you want to squeeze?"))
    print("Here is your", fruits, "glass(es) of juice! 🧃")
except ValueError:
    print("Opps! Please enter a number, not words! 😅")

# 2. Choco Divider 🍫 (Avoid dividing by zero)

try:
    choco = 10
    friends = int(input("How many friends to share with"))
    print("Each friend gets", choco / friends, "chocolates 🍫")
except ZeroDivisionError:
    print("You can't divide chocolate with zero people! 😂")
except ValueError:
    print("Numbers only! friends can't be alphabets. 🙃")

# Secret Code Unlocker 🔏

try:
    code = int(input("Enter the 4-digit secret code: "))
    print("Access Granted 🚪✨")
except ValueError:
    print("That's not a number! Access Denied 🚫")
# Reading Files
# Write some data into a file
file = open("employees.txt", "w")
file.write("Jim - Manager\nPam - Receptionist\nDwight - Salesman")
file.close()


# Read from that file

file = open("employees.txt", "r")

print(file.read())

file.close()


# Challenge 1: Count the Employees

employee_file = open("employees.txt", "r")
lines = employee_file.readlines()
print("Total Employees", len(lines))
employee_file.close()


 Challenge 2: Find the Manager

employee_file = open("employees.txt", "r")
for line in employee_file:
    if "Manager" in line:
        name = line.split("-")[0]
        print("Manager:", name)
employee_file.close()


# Challenge 3: Fancy list
employee_file = open("employees.txt", "r")
for line in employee_file:
    name, job = line.strip().split("-")
    print(f"📝 {name} works as a {job}")
employee_file.close()


# Writing your mood to a file

mood_file = open("mood_log.txt", "w")
mood_file.write("Today I'm feeling super motivated and proud!\n")
mood_file.write("I fixed bugs by myself and did 3 mini projects\n")
mood_file.close()


# Save pizza order
pizza_file = open("pizza_order.txt", "w")
pizza_file.write("1. Margherita with extra cheese\n")
pizza_file.write("2. veggie loaded with mushrooms\n")
pizza_file.write("3. Paneer Tikka pizza\n")
pizza_file.close()


# Save summary of what you learned

summary_file = open("daily_learning.txt", "w")
summary_file.write("I learned about writing files in Python.\n")
summary_file.write("Practiced using open(),write()and close().\n ")
summary_file.write("Next goal: Learn appending and file automation!\n")
summary_file.close()

# Add more moods to the file
mood_file = open("mood_log.txt", "a")
mood_file.write("Feeling excited to learn appending in Python!\n")
mood_file.write("Also feeling like a coding ninja! 🥷\n")
mood_file.close()


# Add new pizza orders
pizza_file = open("pizza_orders.txt", "a")
pizza_file.write("4. Spicy Jalapeno & Corn\n")
pizza_file.write("5. Chocolate Dessert Pizza 🍫🍕")
pizza_file.close()


# Add progress update
summary_file = open("daily_learning.txt", "a")
summary_file.write("✅ Learned how to append text to a file using 'a' mode.\n")
summary_file.write("✅ Practiced without losing old data!\n")
summary_file.close()

# ✅ Check contents of the file
mood_file = open("mood_log.txt", "r")
print(mood_file.read())
mood_file.close()

with open("mood_log.txt", "r") as file:
      for line in file:
        print(line.strip())

