import random
from random import choice


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
           '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
           '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
           '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
           '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
           '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
           '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
           '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']


symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
           '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
           '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
           '}', '~', '!', '"', '#', '$', '%', '&', "'", '(',
           ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
           '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
           '{', '|', '}', '~', '!', '"', '#', '$', '%', '&',
           "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
           ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
           '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator !")
nr_letters = int(input("How many letters would you like in your password "))
nr_symbols = int(input(f"How many symbol would you like ? \n"))
nr_numbers = int(input(f"How many numbers would you like ? \n"))

#password = ""
#for char in range (1,nr_letters +1):
    #password = random.choice(letters)

#for char in range (1,nr_symbols +1):
    #password += random.choice(symbols)

#for char in range (1,nr_numbers +1):
    #password += random.choice(numbers)

#print(password)
#
#password =""
#for char in range (0,nr_letters):
#    password = random.choice(letters)

#for char in range (0,nr_symbols):
#    password += random.choice(symbols)

#for char in range (0,nr_numbers):
#    password += random.choice(numbers)

#print(password)


password_list= []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for char in range (0,nr_symbols):
    password_list.append(random.choice(symbols))

for char in range (0,nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)
password= ""
for char in password_list:
    password += char
print(f"Your password is :{password}")
