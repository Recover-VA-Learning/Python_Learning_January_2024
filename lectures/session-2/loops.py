# region while
# a counter variable to keep track of the number of iterations

# while loop
counter = 0
while counter < 10:
    print(counter)
    counter += 1

# can count down too
count = 10
while count > 0:
    print(count)
    count -= 1
# endregion

# region breaks and continues
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

# a better way to do this
while True:
    n = int(input("What's n? "))
    if n >= 0:
        break
# endregion

# region for

# can use a data type list
for i in [0, 1, 2]:
    print("hi")

for i in range(3):
# range(start, stop, step)
    print("hi")

for _ in range(3):
# range(start, stop, step)
    print("hi")

# endregion
    
# region lists
shapes = ["Square", "Circle", "Triangle"]

print(shapes[0])
print(shapes[1])
print(shapes[2])


for shape in shapes:
    print(shape)

for i in range(len(shapes)):
    print(i + 1, shapes[i])

# endregion
    
# region dictionaries

shapes = ["Square", "Circle", "Triangle"]
colors = ["Red", "Green", "Blue"]

# key value pairs
shapes = {
    "Square": "Red",
    "Circle": "Green",
    "Triangle": "Blue"
}

# access values by key
print(shapes["Square"])
print(shapes["Circle"])
print(shapes["Triangle"])

# iterate over dict gives keys
for shape in shapes:
    print(shape)

# to iterate and get both key and value
for shape in shapes:
    print(shape, shapes[shape])

# lots of data associated many keys

shapes = [
    {
        "name": "Square",
        "color": "Red",
        "sides": 4,
    },
    {
        "name": "Circle",
        "color": "Green",
        "sides": 0,
    },
    {
        "name": "Triangle",
        "color": "Blue",
        "sides": 3,
    }
]

for shape in shapes:
    print(shape["name"], shape["color"], shape["sides"], sep=", ")


