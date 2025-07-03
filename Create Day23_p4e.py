# 1. The classic first program (Module 1)
print("Hello World")

# 2. Greeting program using input() (Module 2)
name = input("Enter your name: ")
print("Hello", name)

# 3. Updating a variable (Module 2 quiz example)
x = 15
x = x + 5
print("Updated x =", x)        # Expected: 20

# 4. Arithmetic expression & PEMDAS (Module 3)
expr_result = 1 + 2 * 3 - 8 / 4
print("Expression result =", expr_result)   # Expected: 5.0

# 5. Remainder (modulo) example (Module 3 quiz)
print("42 % 10 =", 42 % 10)    # Expected: 2

# 6. Pay calculator (Assignments 2.2 / 2.3 – Module 4)
hrs  = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay  = float(hrs) * float(rate)
print("Pay:", pay)
