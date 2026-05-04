# random module and dir function
import random
import bank

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 92, 78, 90, 88]

#dir function
all_functions = dir(random)
print(all_functions)

# choice , randint, random, shuffle, randbytes and seed
#choice
random_name = random.choice(names)
print(f"Randomly selected name: {random_name}")
random_score = random.choice(scores)
print(f"Randomly selected score: {random_score}")
#random
random_number = random.random()
print(f"Random number between 0 and 1: {random_number}")
#randint
random_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_int}")
#shuffle
random.shuffle(names)
print(f"Shuffled names: {names}")
#randbytes
random_bytes = random.randbytes(5)
print(f"Random bytes: {random_bytes}")
#seed
random.seed(2)
random_vote = random.randint(70, 100)
print(f"Random number with seed 0: {random_vote}") 

# python list
 