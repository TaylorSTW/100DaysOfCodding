import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_chars= int(input("How many chars would you like in your password?\n"))
nr_letters = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
nr_symbols = nr_chars - nr_letters - nr_numbers

for chars in range(0, nr_chars):
    local_int = random.randint(0, 2)
    if local_int == 0:
        for char_letters in range(0, 1):
            password.append(random.choice(letters))
    elif local_int == 1:
        for num_number in range(0, 1):
            password.append(random.choice(numbers))
    else:
        if nr_symbols > 0:
            for num_symbols in range(0, 1):
                password.append(random.choice(symbols))

print('Your password is:' + "".join(password))