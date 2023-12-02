

def value_changer():
    global_variables = globals()
    my_dict = {}
    for key, value in global_variables.items():
        if key.endswith('s') and key != 's':
            my_dict[key[ : -1]] = value
            global_variables[key] = None
    for key, value in my_dict.items():
        global_variables[key] = value

datas = [ 42, -73, 12, 85, -15, 2]
s = 'Helloy Worlds'
names = (('NoName'), ('OtherNames'), ('NewName'))
sx = 42
value_changer()
print(globals())








