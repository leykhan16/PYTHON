#Arithmetic Operators
#+	Addition
bill = 100
tip = 20
total = bill + tip
print(total)
#-	Subtraction
difference = bill - tip
print(difference)
#*	Multiplication
product = bill * tip
print(product)
#/	Division
quotient = bill / tip
print(quotient)
#%	Modulus
remainder = bill % tip
print(remainder)
#**	Exponentiation
power = bill ** tip
print(power)
#//	Floor division
floor_division = bill // tip
print(floor_division)
#modulus division
modulus_division = bill % tip
print(modulus_division)
#modulus remainder
modulus_remainder = bill % tip
print(modulus_remainder)
#modulo operator
modulo_result = bill % tip
print(modulo_result)
#control flow statements
#if and else statements
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#comparison operators
# ==	Equal to
x = 5
y = 5
print(x == y)  # True
# !=	Not equal to
print(x != y)  # False
# >	Greater than
print(x > y)   # False
# <	Less than
print(x < y)   # False
# >=	Greater than or equal to
print(x >= y)  # True
# <=	Less than or equal to
print(x <= y)  # True
#conditional statements
#if, elif, and else statements 
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
#conditional staements using input function
user_score = int(input("Enter your score: "))
if user_score >= 90:
    print("Grade: A")
elif user_score >= 80:
    print("Grade: B")
elif user_score >= 70:
    print("Grade: C")
elif user_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
#logical operators
# and, or, not
is_raining = True
is_cold = False
if is_raining and is_cold:
    print("It's raining and cold.")
elif is_raining or is_cold:
    print("It's either raining or cold.")
else:    print("It's neither raining nor cold.")
# toilet mangement system
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
if age < 5:
    print("Use the baby toilet.")
elif age < 12:
    if gender == "M":
        print("Use the boys toilet.")
    else:        print("Use the girls toilet.")
else:
    if gender == "M":
        print("Use the men's toilet.")