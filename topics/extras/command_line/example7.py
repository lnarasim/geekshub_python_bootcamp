import argparse
import datetime

parser = argparse.ArgumentParser(description="Returns a string containing the name and age of the person.")
parser.add_argument('-f', '--first', help='Specify first name', type=str, required=False, dest='first_name')
parser.add_argument('-l', '--last', help="last name", type=str, required=True, dest="last_name")
parser.add_argument('--yob', help="year of birth", type=int, required=False, dest='birth_year')

args = parser.parse_args()
name = (args.first_name or '') + args.last_name
current_year = datetime.datetime.utcnow().year
age = current_year - args.birth_year
print(f'{name} is {age} years old')
