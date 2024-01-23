def print_hi(name):
    print(f'Hi, {name}')


fullName = input("Please enter your name: ")

if "-" in fullName:
    print("Invalid Input")
else:
    print_hi(fullName)
