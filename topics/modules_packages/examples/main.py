import sys

print("===================================================")
print(f'Running main.py - module name {__name__}')

print("importing module1")
import module1
print(module1)
#module1.pprint_dict('main.globals()', globals())

print(sys.path)

print('importing module1 again')
print(sys.modules['module1'])

import module1
print("===================================================")