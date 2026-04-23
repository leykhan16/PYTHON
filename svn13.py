course_title = "Python Programming Mastery"
title2 = "PPM"
new_line = "i am a text  on a new line"
# string manipulation
# string concatenation
complete_course = course_title + " " + title2 + "\n" + new_line
print(complete_course)

# f-string
name = "xtrange"
age = 25
role = "i am a Rust and Python engineer"
#info = "My name is " + name + "i'm" + age + "yrs old" + "a" + role
#print(info)
info_with_fstring = f"My name is {name}, I'm {age} years old, and {role}"
print(info_with_fstring)    

# python primitive data types
#string
name = "xtrange"
print(name)
#integer
age = 25
print(age)
#float
height = 5.9
print(height)
#boolean
is_student = True
print(is_student)
#type checking
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
# using underscore for improved readability
large_number = 1_000_000
print(large_number)

#datatype conversion
# converting string to integer
age_str = "25"
age_int = int(age_str)
print(age_int)
# converting integer to string
age_str_again = str(age_int)
print(age_str_again)
# converting string to float
height_str = "5.9"
height_float = float(height_str)
print(height_float)
# converting float to string
height_str_again = str(height_float)
print(height_str_again)
#converting boolean to string
is_student_str = str(is_student)
print(is_student_str)

#python input function
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")