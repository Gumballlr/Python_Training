import random

chars = 'qwertyuiopasdfghjklzxcvbnm1234567890.'
while True:
    try:
        length = int(input('Input your length password:'))
        break
    except ValueError:
        print("Please enter a valid number")
password = ''
for i in range(length):   
    password += random.choice(chars)
print(password)
