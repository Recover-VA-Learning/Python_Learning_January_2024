import sys

print(f"Arguments: {sys.argv}")
print(f"Arguments: {sys.argv[1]}")
print(f"Arguments: {sys.argv[2]}")

try:
    print(int(sys.argv[1]) + int(sys.argv[2]))
except ValueError:
    print("Invalid arguments")
    sys.exit(1)