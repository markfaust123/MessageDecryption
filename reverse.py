"""
Created on Thu Jan  5

@author: Mark Faust (JHED: mfaust4)
"""



# Project 1 - Problem A



# Declaration of a list containing all of the letters of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', \
            'y', 'z']
    
# Declares an empty string 
decrypted = ""

# Asks for encryption input
encrypted = input("Enter the encrypted message: ")

# Iterates through each letter in the encrypted message
for letter in encrypted:

    # Determines ASCII value of each letter
    num = ord(letter)
    # Determines letter's associated index in alphabet
    dist_from_a = num - 97
        
    # Only allows for alphabetic characters to be decrypted
    if ord(letter) >= 97 and ord(letter) <= 122:
        decrypted += alphabet[25 - dist_from_a]
    # Leaves alone non-alphabetic characters
    else:
        decrypted += letter

# Prints out decrypted message
print("The plaintext message is:", decrypted)

