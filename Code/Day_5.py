If statement comparison

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))

Another comparison

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

Dictionaries

monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December",
}


print(monthConversions.get("Luv", "Not a valid key"))

While Loop


i = 1
while i <= 10:
  print(i)
  i += 1

print("Done with loop")

Building a Guessing Game
secret_number = 7
guess = 0

while guess != secret_number:
  guess = int(input("Enter your guess"))
  if guess != secret_number:
    print("Wrong! Try again.")

print("Congratulations!")

Another Guessing Game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
