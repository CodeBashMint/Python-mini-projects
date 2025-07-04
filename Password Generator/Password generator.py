import random
import string

# Character sets
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("--- Welcome to the password Generator program ---")

# Get user input with validation
try:
    n_letters = int(input("Enter how many letters do you want in your password?\n"))
    n_numbers = int(input("Enter how many numbers do you want in your password?\n"))
    n_symbols = int(input("Enter how many symbols do you want in your password?\n"))
except ValueError:
    print("Please enter valid numbers only.")
    exit()

# Combine characters
password_list = []

for i in range(n_letters):
    password_list.append(random.choice(letters))

for i in range(n_numbers):
    password_list.append(random.choice(numbers))

for i in range(n_symbols):
    password_list.append(random.choice(symbols))

# Shuffle the list to randomize character order
random.shuffle(password_list)

# Join characters to make the final password string
password = ''.join(password_list)

# Print the final password
print("\nYour generated password is:")
print(password)

# Check password strength
total_length = n_letters + n_numbers + n_symbols

print("\nPassword Strength:")
if total_length < 6:
    print("Weak (consider using more characters)")
elif total_length < 10:
    print("Moderate")
else:
    print("Strong")

