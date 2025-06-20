# Day 10 - Practicing Object Functions in Python

# 1. Dog class with bark, sit, and roll_over
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof woof!")

    def sit(self):
        print(f"{self.name} is now sitting 🪑")

    def roll_over(self):
        print(f"{self.name} rolled over! 🍥")

my_dog = Dog("Rocky", "Labrador")
my_dog.bark()
my_dog.sit()
my_dog.roll_over()


# 2. Rabbit class with jump and eat
class Rabbit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def jump(self):
        print(f"{self.name} the {self.color} bunny jumps high! 🐇")

    def eat(self, food):
        print(f"{self.name} is munching on {food} 🥕")

my_rabbit = Rabbit("Snowball", "white")
my_rabbit.jump()
my_rabbit.eat("carrots")


# 3. Student class with result feedback
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_result(self):
        print(f"{self.name} scored {self.grade} marks.")

        if self.grade >= 90:
            print("🏆 Excellent work!")
        elif self.grade >= 75:
            print("👏 Good job!")
        else:
            print("📚 Keep practicing!")

s1 = Student("Imad", 92)
s2 = Student("Nylah", 76)

s1.show_result()
s2.show_result()
