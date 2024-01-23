import random
import string

print("Welcome to this Password Generator!")
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#@!%().,'
length=int(input("What is the length of the password you want?: "))
password=''
for char in range(length):
    password += random.choice(chars)

print("Here is Your Password: " + password) 