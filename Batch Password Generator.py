#this is a password generator
import random, sys

#the character selection list
characters = "abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&*"

while True:
    number_of_passwords = int(input('How many passwords will you be needing?: ')) # total number of passwords
    if number_of_passwords <2:
        password_length = int(input('How many characters would you like your password to be?: ')) # get users desired password length
    else:
        password_length = int(input('How many characters would you like your passwords to be?: ')) # get users desired password length

    for i in range(number_of_passwords):
        password = '' .join(random.sample(characters, password_length)) # makes a random selection from the available characters list
        print(password)
    if number_of_passwords < 2:
        repeat = input('Here is your ' + str(number_of_passwords)  + ' password! Do you need more? y or n: ')
        if repeat == 'y':
            continue
        elif repeat == 'n':
            sys.exit()
    else:
        repeat = input('Here are your ' + str(number_of_passwords)  + ' passwords! Do you need more? y or n: ')
        if repeat == 'y':
            continue
        elif repeat == 'n':
            sys.exit()
