# python list
first_list = []
print(type(first_list))

# uing a list constructor function
second_list = list()
print(type(second_list))

class_list = ["chris", "michael", "sarah", "jessica"]
print(type(class_list))
#indexing and slicing lists
print(class_list[0])  # chris
print(class_list[1])  # michael
print(class_list[2])  # sarah
print(class_list[3])  # jessica

#negative indexing
print(class_list[-1])  # jessica
print(class_list[-2])  # sarah
print(class_list[-3])  # michael
print(class_list[-4])  # chris

#slicing lists
print(class_list[0:2])  # ['chris', 'michael']
print(class_list[1:3])  # ['michael', 'sarah']
print(class_list[2:4])  # ['sarah', 'jessica']
print(class_list[:2])   # ['chris', 'michael']
print(class_list[2:])   # ['sarah', 'jessica']

#python index error and len() function
programming_languages = ["python", "java", "c++", "javascript", "ruby", "go", "swift", "kotlin", "php", "typescript"]
#index error
#print(programming_languages[10])  # IndexError: list index out of range
print(len(programming_languages))  # 10
print(programming_languages[9])    # typescript

#updating list items
programming_languages[0] = "python3"
print(programming_languages[0])    # python3

#python list operations
sequence = [True, "John", [56,78], "chris", [True, ["shadrach", "John",78], 90.66]]
cart = ["Macbook", "airpod", "toilet paper", "baking powder"]
# usig the dir function to see the available methods for list
print(dir(cart))