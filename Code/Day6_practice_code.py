# If-Else Fruits Practice

apple_is_sweet = True
if apple_is_sweet:
    print("I eat the apple.")
else:
    print("No apple today.")

# raise_to_power function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))

# pizza_slices function

def pizza_slices(pizza_count, slices_per_pizza):
    total_slices = pizza_count * slices_per_pizza
    return total_slices

print(pizza_slices(3, 8))

# Animal Translator

def animal_translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation += "🐶"
        else:
            translation += letter
    return translation 

print(animal_translator(input("Say something: ")))

# Emoji Translator

def emoji_translator(message):
    translation = ""
    for char in message:
        if char == ":)":
            translation += "😊"
        elif char == ":(":
            translation += "🤪"
        else:
            translation += char
    return translation

print(emoji_translator(input("Enter your message: ")))

# 2D List Nested Loops Practice

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

# While Loop Guessing Game

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
