import csv
import json
from pathlib import Path

# Folder for files created by the file-handling exercises (18, 19, 20)
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def header(number, title):
    print(f"\n=== Exercise {number}: {title} ===")



# Exercise 11: Lists - basic operations

def exercise_11():
    header(11, "List Operations")
    fruits = ["apple", "banana", "cherry"]
    print("Original:", fruits)
    fruits.append("mango")
    print("After append:", fruits)
    fruits.insert(1, "orange")
    print("After insert at index 1:", fruits)
    fruits.remove("banana")
    print("After remove 'banana':", fruits)
    fruits.sort()
    print("Sorted:", fruits)
    print("First:", fruits[0], "| Last:", fruits[-1])
    print("Length:", len(fruits))



# Exercise 12: Lists - statistics (max, min, average)

def exercise_12():
    header(12, "List Statistics")
    scores = [72, 88, 95, 60, 79, 91]
    print("Scores:", scores)
    print("Maximum:", max(scores))
    print("Minimum:", min(scores))
    print("Sum:", sum(scores))
    print("Average:", round(sum(scores) / len(scores), 2))
    print("Sorted high to low:", sorted(scores, reverse=True))



# Exercise 13: List comprehension and tuples

def exercise_13():
    header(13, "List Comprehension and Tuples")
    squares = [x ** 2 for x in range(1, 11)]
    evens = [x for x in range(1, 21) if x % 2 == 0]
    print("Squares 1-10:", squares)
    print("Evens 1-20:", evens)

    point = (3, 4)  # tuple: cannot be changed
    x, y = point
    print(f"Point: x={x}, y={y}")
    print("Distance from origin:", (x ** 2 + y ** 2) ** 0.5)



# Exercise 14: Dictionaries

def exercise_14():
    header(14, "Dictionaries")
    student = {"name": "Asha", "age": 20, "course": "ML"}
    print("Student:", student)
    student["city"] = "Bharatpur"
    student["age"] = 21
    print("After update:", student)
    print("Name:", student["name"])
    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))
    for key, value in student.items():
        print(f"  {key} -> {value}")



# Exercise 15: Sets and word frequency

def exercise_15():
    header(15, "Sets and Word Frequency")
    numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    print("Unique numbers:", set(numbers))

    sentence = "the cat and the dog and the bird"
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    print("Word frequency:", freq)



# Exercise 16: Functions - basics

def exercise_16():
    header(16, "Functions")

    def add(a, b):
        return a + b

    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    print("add(3, 4) =", add(3, 4))
    print(greet("Asha"))
    print(greet("Asha", "Namaste"))
    print("Primes up to 30:", [n for n in range(1, 31) if is_prime(n)])



# Exercise 17: Functions - *args, recursion, lambda

def exercise_17():
    header(17, "Advanced Functions")

    def total(*numbers):
        return sum(numbers)

    def factorial(n):
        return 1 if n <= 1 else n * factorial(n - 1)

    square = lambda x: x ** 2

    print("total(1, 2, 3, 4) =", total(1, 2, 3, 4))
    print("factorial(5) =", factorial(5))
    print("square(9) =", square(9))
    print("Sorted by length:", sorted(["pear", "fig", "banana"], key=len))



# Exercise 18: File handling - text file

def exercise_18():
    header(18, "Text File Handling")
    path = DATA_DIR / "notes.txt"

    with open(path, "w") as f:
        f.write("Week 1: Python basics\n")
        f.write("Week 2: NumPy and pandas\n")
    with open(path, "a") as f:
        f.write("Week 3: Visualization and EDA\n")

    with open(path, "r") as f:
        lines = f.readlines()

    print("Number of lines:", len(lines))
    for number, line in enumerate(lines, start=1):
        print(f"  {number}. {line.strip()}")



# Exercise 19: File handling - CSV

def exercise_19():
    header(19, "CSV Handling")
    path = DATA_DIR / "students.csv"

    rows = [
        {"name": "Asha", "marks": 88},
        {"name": "Ravi", "marks": 72},
        {"name": "Sita", "marks": 95},
    ]

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "marks"])
        writer.writeheader()
        writer.writerows(rows)

    with open(path, "r") as f:
        data = list(csv.DictReader(f))

    marks = [int(row["marks"]) for row in data]
    for row in data:
        print(f"  {row['name']}: {row['marks']}")
    print("Average marks:", round(sum(marks) / len(marks), 2))



# Exercise 20: File handling - JSON

def exercise_20():
    header(20, "JSON Handling")
    path = DATA_DIR / "students.json"

    students = [
        {"name": "Asha", "skills": ["Python", "SQL"]},
        {"name": "Ravi", "skills": ["Python"]},
    ]

    with open(path, "w") as f:
        json.dump(students, f, indent=4)

    with open(path, "r") as f:
        loaded = json.load(f)

    for s in loaded:
        print(f"  {s['name']} knows: {', '.join(s['skills'])}")
    print("Total students:", len(loaded))



if __name__ == "__main__":
    exercise_11()
    exercise_12()
    exercise_13()
    exercise_14()
    exercise_15()
    exercise_16()
    exercise_17()
    exercise_18()
    exercise_19()
    exercise_20()