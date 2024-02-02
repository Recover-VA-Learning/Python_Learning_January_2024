# import module
import random
# from random import choice

result = random.choice(['heads', 'tails'])
print(result)

dice = random.randint(1, 6)
print(dice)

shuffled = [1, 2, 3, 4, 5, 6]
random.shuffle(shuffled)
print(shuffled)
