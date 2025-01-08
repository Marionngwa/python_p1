# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# password = ""
# print("welcome to the password generator ")
# num_l = int(input(f"How many letters would you like in your password?\n "))
# num_symbol = int(input(f"How many symbols would you like in this password ?\n "))
# _num = int(input(f"How many numbers would you like in this password ?\n "))

# password = ""

# for x in range(1, num_l +1):
#     password += random.choice(letters)


# for x in range(1, num_symbol +1):
#     password += random.choice(numbers)


# for x in range(1, _num +1):
#     password += random.choice(symbols)
# print(password)

#sol 2

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""
print("Welcome to the Password Generator!")
num_l = int(input("How many letters would you like in your password?\n"))
num_symbol = int(input("How many symbols would you like in your password?\n"))
num = int(input("How many numbers would you like in your password?\n"))

# Create a list to hold all characters
password_list = []


for _ in range(num_l):
    password_list.append(random.choice(letters))

# Add symbols to the list
for _ in range(num_symbol):
    password_list.append(random.choice(symbols))


for _ in range(num):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)


password = "".join(password_list)

print(f"Your password is: {password}")
