import common.validators

common.validators.boolean.is_boolean('123')

print('\n\n****self***')

for k in dict(globals()).keys():
    print(k)

print('\n\n****common***')

for k in common.__dict__.keys():
    print(k)

print('\n\n****validators***')

for k in common.validators.__dict__.keys():
    print(k)

print('\n\n****numeric***')
for k in common.validators.numeric.__dict__.keys():
    print(k)