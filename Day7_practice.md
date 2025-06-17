# 🌟 Day 7, Python Learning Log - 17 June 2025

## ✅ Topics I Practiced Today

### 1. 📝 Comments in Python
- Learned how to use `#` to write comments in code.
- Python ignores comments; they're helpful for explaining or organizing code.
```python
# This is a comment
print("Hello!")  # This is also a comment

### 2. ⚠️ Try-Except Error Handling**

Learned to stop program crash with try-except.

Tried fun codes like:
Juice Squeezer (ZeroDivisionError)
Choco Divider (ValueError)
Secret Code

    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Enter a valid number.")


3. 📖 Reading from Files
Used open("file.txt", "r") and .readline(), .read(), and loop to print.

Used .strip() to remove extra lines/spaces.


4. 🖊️ Writing to Files
Used "w" mode to write new content to file.

Saved mood logs, pizza orders, and what I learned.

with open("pizza_order.txt", "w") as file:
    file.write("1 Cheese Pizza\n")


5. 📎 Appending to Files
Used "a" mode to add data without deleting old content.
with open("mood_log.txt", "a") as file:
    file.write("Feeling super smart today!\n")
🤯 Challenges I Faced
Confusion about indentation (space/tab) before def, if, else, for, return.

Spelling errors like Print, riase, colse, ttranslation.

Forgetting colons : or quotes "".

💡 How I Solved Them
Observed indentation examples closely and corrected spacing.

Practiced slowly and repeated code until it worked.

Took help from you (ChatGPT 😊) and fixed small mistakes myself.

⏳ Time Spent
🎥 Watched FreeCodeCamp video: 28 minutes

👩‍💻 Practiced manually in Google Colab: 3+ hours

✍️ Did 3 fun extra codes on each topic to make it stick.

💖 Motivation
"I don’t have to be perfect. I just have to keep going. Every bug is a lesson, and every fix is a win! Today I feel confident, creative, and curious!
Day by day everyday I am getting better better and better!"

🚀 What’s Next?
Practice more on functions and file-based projects with real ideas.
