# module1.py

print(f'----------Running {__name__}---------')

def pprint_dict(header, d):
    print('\n\n--------------------------------------')
    print(f'****** {header} ******')
    for k, v in d.items():
        print(k, v)
    print(f"-----------------------------------------\n\n")

pprint_dict('module_global', globals())

print(f'---------- End of {__name__}---------')
