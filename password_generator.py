
# This program is a python password generation program

import random

letters = ['a', ' b', ' c', ' d', ' e', ' f', ' g', ' h', ' i', ' j', ' k', ' l', ' m', ' n', ' o', ' p', ' q', ' r', ' s', ' t', ' u', ' v', ' w', ' x', ' y', ' z', 'A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' I', ' J', ' K', ' L', ' M', ' N', ' O', ' P', ' Q', ' R', ' S', ' T', ' U', ' V', ' W', ' X', ' Y', ' Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print()
print('Welcome to the PyPassword Generator!')
print()

nr_letters = int(input('How many letters would you like in your password?\n'))
print()

nr_symbols = int(input(f'How many symbols would you like?\n'))
print()

nr_numbers = int(input(f'How many numbers would you like?\n'))
print()

len_let = len(letters)
len_num = len(numbers)
len_sym = len(symbols)

gen_let = random.randint(0, len_let -1)
gen_num = random.randint(0, len_num -1)
gen_sym = random.randint(0, len_sym -1)

