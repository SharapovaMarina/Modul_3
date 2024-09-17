def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25, c = [1,2,3])

values_list = ["string", 25, True]
values_dict = {"a": "string", "b": False, "c": 25}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

