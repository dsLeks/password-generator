import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

# i = 0
# flag = False
# while i < total_length:
#     random_input = random.choice(possible_inputs)
#     if random_input == letters and nr_letters > 0:
#         nr_letters -= 1
#         password += random.choice(letters)
#         flag = True
#     if random_input == numbers and nr_numbers > 0:
#         nr_numbers -= 1
#         password += random.choice(numbers)
#         flag = True
#     if random_input == symbols and nr_symbols > 0:
#         nr_symbols -= 1
#         password += random.choice(symbols)
#         flag = True
#     if flag == True:
#         i += 1
#         flag = False
