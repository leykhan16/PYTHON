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