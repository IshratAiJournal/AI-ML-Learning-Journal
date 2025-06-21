# Day 11 - 21 June 2025 Practicing Python Interpreter Behavior

# 1. Inheritance

class person:
    def __init__(self, name):
        self.name = name

class student(person):
    def study(self):
        print(f"{self.name} is studying 📚")

class Teacher(person):
    def teach(self):
        print(f"{self.name} is teaching 🧑‍🏫")

s = student("Imad")
t = Teacher("Ishrat")

s.study()
t.teach()

# 2. Rabbit Class that Eats and Jumps

class Rabbit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def jump(self):
        print(f"{self.name} the {self.color} bunny jumps high! 🐰")


    def eat(self, food):
        print(f"{self.name} is munching on {food} 🥕")

my_rabbit = Rabbit("snowball", "white")
my_rabbit.jump()
my_rabbit.eat("carrots")

# 1. Understanding Python Interpreter - Line by Line Execution
print("Line 1: Starting the program...")
a = 10
print("Line 2: a =", a)
b = 20
print("Line 3: b =", b)
c = a + b
print("Line 4: c = a + b =", c)

# Students with grade and feedback

class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_result(self):
        print(f"{self.name} scored {self.grade} marks.")


        if self.grade >= 90:
            print(" 🏆 Excellent work!")
        elif self.grade >= 75:
            print(" 👏 Good job!")
        else:
            print("📚 Keep practicing!")

# 4. Class: Vehicle with Inheritance
     
class Vehicle:
      def __init__(self, brand):
          self.brand = brand

      def move(self):
          print(f"{self.brand} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} car is driving.")

class Bike(Vehicle):
    def move(self):
        print(f"{self.brand} bike is riding 🚵")


c = Car("Honda")
b = Bike("Yamaha")

c.move()
b.move()


# 5.. Interpreter Stops at Error (Intentional mistake to show behavior)
print("\nHello!")
x = 5
y = 0
# Uncommenting the next line will cause an error and stop the interpreter
# z = x / y
# print("This will not print")


# 6. Try-Except to keep interpreter running
print("\nTrying division safely...")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero!")

print("But the program is still running 😅")
