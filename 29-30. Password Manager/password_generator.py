# Password Generator Project
from random import choice, shuffle, randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [choice(letters) for char in range(randint(6, 10))]
password_symbols = [choice(symbols) for sym in range(randint(2, 6))]
password_numbers = [choice(numbers) for num in range(randint(2, 6))]

password_list = password_letters + password_symbols + password_numbers
shuffle(password_list)

password = "".join(password_list)
for char in password_list:
    password += char
