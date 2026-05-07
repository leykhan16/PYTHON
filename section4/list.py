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
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#append() method
cart.append("eggs")
print(cart)  # ['Macbook', 'airpod', 'toilet paper', 'baking powder', 'eggs']
cart.append("milk")
print(cart)  # ['Macbook', 'airpod', 'toilet paper', 'baking powder', 'eggs', 'milk']
#clear() method
cart.clear()
print(cart)  # []
#copy() method
new_cart = ["Macbook", "airpod", "toilet paper", "baking powder"]
cart_copy = new_cart.copy()
print(cart_copy)  # ['Macbook', 'airpod', 'toilet paper', 'baking powder']
#count() method
print(cart_copy.count("Macbook"))  # 1
print(cart_copy.count("airpod"))   # 1
#extend() method
cart_copy.extend(["eggs", "milk"])
print(cart_copy)  # ['Macbook', 'airpod', 'toilet paper',
#it's important to note that the extend() method modifies the original list and does not return a new list. Therefore, it does not return anything (i.e., it returns None). If you try to print the result of cart_copy.extend(["eggs", "milk"]), it will print None because the method itself does not return a value. However, after calling extend(), the cart_copy list will be updated with the new items.
#index() method
print(cart_copy.index("toilet paper"))  # 2
print(cart_copy.index("eggs"))          # 4
#insert() method
cart_copy.insert(2, "hand sanitizer")
print(cart_copy)  # ['Macbook', 'airpod', 'hand sanitizer', 'toilet paper', 'baking powder', 'eggs', 'milk']
#pop() method
popped_item = cart_copy.pop()
print(popped_item)
#remove() method
cart_copy.remove("hand sanitizer")
print(cart_copy)  # ['Macbook', 'airpod', 'toilet paper', 'baking powder', 'eggs', 'milk']
#reverse() method
cart_copy.reverse()
print(cart_copy)  # ['milk', 'eggs', 'baking powder', 'toilet paper', 'hand sanitizer', 'airpod', 'Macbook']
#sort() method
cart_copy.sort()
print(cart_copy)  # ['Macbook', 'airpod', 'baking powder', 'eggs', 'hand sanitizer', 'milk', 'toilet paper']

#python nested list
sequence = [True, "John", [56,78], "chris", [True, ["shadrach", "John",78], 90.66]]
last_item = sequence[-1]
nested_item = last_item[1]
last_item_of_nested_list = nested_item[-1]
print(last_item_of_nested_list)
print(nested_item)
print(last_item)
print(sequence[-1][1][-1])