import os

# Get the current working directory
print(os.getcwd())

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(f"Current Path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}")
    print()

# only get txt files
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for file in filenames:
        if file.endswith(".txt"):
            print(os.path.join(dirpath, file))
            target_file = os.path.join(dirpath, file)

# get file size
print(os.path.getsize(target_file))

# read file content
with open(target_file, "r") as f:
    print(f.read())

# get the hash of the file
import hashlib

def get_hash(file):
    hasher = hashlib.md5()
    with open(file, "rb") as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

print(get_hash(target_file))