import random
# Mini Challenge how to get the result of 100 coin flips, 1000, 10000, 100000, 1000000
# Hint: use a loop and a list

# region Pseudocode
# 1. Create a list to store the results
# 2. Create a loop to flip the coin
# 3. Store the result in the list
# 4. Count the number of heads and tails
# endregion

# region Code
# 1. Create a list to store the results
results = []

# 2. Create a loop to flip the coin
for i in range(10000):
    result = random.choice(['heads', 'tails'])
    results.append(result)

# 4. Count the number of heads and tails
print(f"Heads: {results.count('heads')}\t Tails: {results.count('tails')}")
# endregion

