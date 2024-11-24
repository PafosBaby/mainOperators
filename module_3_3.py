
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25 , c = [1,2,3])

values_list = ['string', 128, True]
values_dict = {'a': 9, 'b': False, 'c': 'STRING'}
values_list_2 = ['test' , 42]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 55)