def header(number, title):
    print(f"\n=== Exercise {number}: {title} ===")


# Exercise 1: Variables and data types

def exercise_1():
    header(1, "Personal Information")
    name = "Kushal Adhikari"
    age = 21
    height_cm = 170.5
    is_student = True

    print("Name:", name)
    print("Age:", age)
    print("Height (cm):", height_cm)
    print("Is student:", is_student)
    print(f"My name is {name}, I am {age} years old, {height_cm} cm tall, "
          f"and it is {is_student} that I am a student.")
    print("Type of name:", type(name))
    print("Type of age:", type(age))
    print("Type of height_cm:", type(height_cm))
    print("Type of is_student:", type(is_student))


# Exercise 2: Arithmetic operators

def exercise_2():
    header(2, "Arithmetic Operators")
    a, b = 17, 5
    print("a =", a, " b =", b)
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor division:", a // b)
    print("Modulus (remainder):", a % b)
    print("Power:", a ** 2)


# Exercise 3: Strings and string methods

def exercise_3():
    header(3, "String Methods")
    text = "  Machine Learning Internship  "
    print("Original:", repr(text))
    print("Stripped:", repr(text.strip()))
    print("Upper:", text.strip().upper())
    print("Lower:", text.strip().lower())
    print("Length:", len(text.strip()))
    print("Replace:", text.strip().replace("Internship", "Journey"))
    print("Split:", text.strip().split())
    print("First 7 chars:", text.strip()[:7])
    print("Reversed:", text.strip()[::-1])
    print("Starts with 'Machine'?", text.strip().startswith("Machine"))


# Exercise 4: User input

def exercise_4():
    header(4, "User Input")
    name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year: "))
    current_year = 2026
    age = current_year - birth_year
    print(f"Hello {name}! You are about {age} years old.")


# Exercise 5: if / else - even or odd

def exercise_5():
    header(5, "Even or Odd")
    for number in [7, 12, 0, -3]:
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")


# Exercise 6: if / elif / else - grade calculator

def exercise_6():
    header(6, "Grade Calculator")
    for marks in [95, 82, 67, 45, 30]:
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"
        print(f"Marks: {marks} -> Grade: {grade}")


# Exercise 7: Logical operators - leap year

def exercise_7():
    header(7, "Leap Year Checker")
    for year in [1900, 2000, 2024, 2026]:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")


            
# Exercise 8: for loop - multiplication table

def exercise_8():
    header(8, "Multiplication Table")
    n = 7
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")



# Exercise 9: while loop - sum of digits

def exercise_9():
    header(9, "Sum of Digits")
    number = 12345
    original = number
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    print(f"Sum of digits of {original} is {total}")



# Exercise 10: Loops - FizzBuzz

def exercise_10():
    header(10, "FizzBuzz (1 to 20)")
    for i in range(1, 21):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()    
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()