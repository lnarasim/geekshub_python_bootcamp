import argparse

parser = argparse.ArgumentParser(description='prints the squares of a list of numbers and the cubes of another list of numbers')
parser.add_argument('--sq', help='list of numbers to square', nargs='*', type=float)
parser.add_argument('--cu', help='list of numbers to cube', nargs='+', type=float, required=True)

args = parser.parse_args()

if args.sq:
    square = [n ** 2 for n in args.sq]
    print(square)

cubes = [n ** 3 for n in args.cu]
print(cubes)