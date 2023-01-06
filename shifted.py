"""
Created on Thu Jan  5

@author: Mark Faust (JHED: mfaust4)
"""

# Project 1 - Problem B



# Algorithm to analyze the pride_prejudice.txt file to gather data to caluculate
# letter likelihood values



# Open file titled sample.txt
pride_prejudice = open('pride_prejudice.txt', 'r', encoding='utf-8-sig')

# Declare variable to count number of letters in the entire file 
M = 0


# declaring parallel lists with indices that correspond to the letters in the 
# alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', \
            'y', 'z']

# x_a contains letter frequency
x_a = [0 for i in range(26)]
# p_a contains letter likelihood
p_a = [0 for i in range(26)]

# Iterate through each line in pride_prejudice
for line in pride_prejudice:

    # Counting how many of each letter and the total number
    # of letters there are in the entire text
    for letter in line:
        if ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122:
            # Counts how many total letters
            M += 1
            # Counts how many of each individual letter and puts value in x_a
            dist_from_a = ord(letter.lower()) - 97
            x_a[dist_from_a] += 1

# Close the file
pride_prejudice.close()

# Calculates each letter's likelihood of appearing in the language using the 
# given formula
for i in range(26):
    p_a[i] = x_a[i] / M



# Algorithm to read encrypted message and produce all possible shifted decryptions



# Analyzing the inputted string
decrypted = ""
# Declares a list to contain all the possible decryptions
possibilities = ["" for i in range(26)]
# Prompts for encrypted message
encrypted = input("Enter the encrypted message: ")

# Iterates through each possible shifted_by value
for shifted_by in range(26):

    # Iterates through each letter in the encrypted message
    for letter in encrypted:
        
        # Determines appropriate index for 
        dist_from_a = ord(letter) - 97
        
        # Algorithm to shift individual letters of the encrypted message by 
        # shifted_by and placing them in a temorary string decrypted
        if ord(letter) >= 97 and ord(letter) <= 122:
            if dist_from_a >= shifted_by:
                decrypted += chr(ord(letter) - shifted_by)
            else:
                decrypted += chr(ord(letter) + 26 - shifted_by)
        else:
            decrypted += letter
    # Placing the shifted decryptions into possibilities
    possibilities[shifted_by] = decrypted
    # Resets decrypted
    decrypted = ""

# Declare variable to count number of letters in each decryption 
N = 0

# Declare list to hold the number of letters in each possible decryption
n_a = [0 for i in range(26)]
# Declare list to hold the chi values for each possible decryption
chis = [0.0 for i in range(26)]

chi = 0



# Algorithm to calculate the chi values for each possible decryption



# Iterates through each index i for different lists
for i in range(26):
    
    # Iterates through each letter of the possible decryption at index i
    # of possibilities
    for letter in possibilities[i]:

        # Counting how many of each letter and the total number
        # of letters there are in the decryption at index i of possibilities
        if ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122:
            # Counts how many total letters           
            N += 1
            # Counts how many of each individual letter and puts value in x_a
            dist_from_a = ord(letter.lower()) - 97
            n_a[dist_from_a] += 1
            
    # Calculates the chi value for each decryption by using the given summation
    # equation and each decryption's unique n_a list containing its 
    # letter frequencies
    for j in range(len(n_a)):
        # Utilization of the parallel array p_a from earlier which contains
        # letter likelihood
        chi += ((n_a[j] - p_a[j] * N) ** 2) / (p_a[j] * N)
    
    # Enters the chi value for the decryption at index i of possibilities into
    # index i of chis
    chis[i] = chi
    # Reset variables and list for use by next possible decryption
    chi = 0
    N = 0
    # Resets n_a because next decryption has different number of each letter
    n_a = [0 for i in range(26)]
    
    

# Algortihm to print out which of the 26 decryptions has the lowest chi value,
# meaning it is most likely to be correct decryption



index = 0
low = chis[0]

# Iterates through each chi value in chis
for i in range(len(chis)):
    
    # Comparing decryption chi values to determine which has the lowest
    if chis[i] < low:
        # Stores index of lowest chi value for future use
        index = i
        low = chis[index]

# Prints most-likely decryption at index index form list possibilities
print("The plaintext message is:", possibilities[index])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    