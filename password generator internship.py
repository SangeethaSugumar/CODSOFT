#import random module from the python library
import random

#import string module from the python library
import string

#creating variable for the each and every letters for the password generator.
individual_letters = string.ascii_letters
numbers = string.digits
different_characters= string.punctuation
total = individual_letters + numbers+ different_characters

#creating a variable length_of_password for getting input from the user
length = int(input("Enter the length of the password you want: "))

#generating password for the getting a password
generated_password = ''.join(random.choices(total, k= length))

#finally the password is generated
print("The generated password is:",generated_password)
