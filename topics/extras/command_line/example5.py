import sys

args = {}

keys = sys.argv[1::2]
values = sys.argv[2::2]

args = {k: v for k, v in zip(keys, values)}
first_name = args.get('--first-name', None)
last_name = args.get('--last-name', None)
yob = int(args.get('--yob', None))

print(first_name, last_name, yob)