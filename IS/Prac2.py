plaintext = "No good deed will go unpunished"
key = 8

ciphertext = [''] * key  # List to hold strings for each row

# The error was because you should be adding to ciphertext[column] not ciphertext[pointer]
for column in range(key):
    pointer = column

    while pointer < len(plaintext):
        ciphertext[column] += plaintext[pointer]  # Add characters in same row
        pointer += key  # Move pointer by key to simulate the "zigzag"

# Join all strings from the ciphertext list to form the final ciphered text
print(''.join(ciphertext))