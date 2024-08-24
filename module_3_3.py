def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_dict = [2, 'Робот', True]
values_list = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_dict)
print_params(**values_list)

values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)