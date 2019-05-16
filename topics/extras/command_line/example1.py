import sys

print("Hello")
print(sys.argv)

for val in sys.argv:
    print(val, type(val))