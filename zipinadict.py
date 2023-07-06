headers = ['name', 'age', 'species']
row1 = ['Duke', 12, 'dog']

my_dict = {}
x = zip(headers, row1)

for item in x:
    my_key = item[0]
    my_value = item[1]
    my_dict[my_key] = my_value
print(my_dict)
