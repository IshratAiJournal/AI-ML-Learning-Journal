# Day 24 - Python Conditional Exercises
# Date: 4 July 2025
# Module 5: Conditional Execution

# 🚀 Exercise 1: Gross Pay Calculator with Overtime

# Get input from user
hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")

# Convert to float
h = float(hrs)
r = float(rate)

# Calculate pay including overtime
if h <= 40:
    pay = h * r
else:
    pay = 40 * r + (h - 40) * r * 1.5

print("Pay:", pay)  # Example input: 45, 10.5 → Output: 498.75


# 🚀 Exercise 2: Score to Grade Conversion

score_input = input("Enter Score: ")

try:
    score = float(score_input)
except ValueError:
    print("Error: input is not a number")
    quit()

# Validate score range
if score < 0.0 or score > 1.0:
    print("Error: score out of range (0.0 - 1.0)")
    quit()

# Determine grade
if score >=
