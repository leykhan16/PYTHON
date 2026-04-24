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
#inverse of boolean values
is_raining = True
is_not_raining = not is_raining
print(is_not_raining)  # False
is_cold = False
is_not_cold = not is_cold
print(is_not_cold)  # True 
#nested if else statements
number = int(input("Enter a number: "))
# creating conditional statement
if number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
else:    print("The number is positive.")

# outer/top conditional statement
user_response = input("are you hungry? (yes/no): ")
if user_response == "yes":
    print("Go to the grocery store.")
    chocolate_price = float(input("how much is the chocolate? "))
    if chocolate_price <= 5:
        print("Buy the 3 chocolates.")
    else:
        print("Buy the 1 chocolate.")
elif user_response == "no":
    print("stay at home.")
    fortnite = input("do you want to play fortnite? (yes/no): ")
    if fortnite == "yes":  
        print("see you next week.")
    elif fortnite == "no":
        print("go to study.")
        subject = input("which subject do you want to study? (math/science/english): ")
        if subject == "math":
            print("study math.")
        elif subject == "science":
            print("we have nothing is common.")
    else:
        print("invalid response. please enter 'yes' or 'no'.")
else:
    print("Invalid response. Please enter 'yes' or 'no'.")