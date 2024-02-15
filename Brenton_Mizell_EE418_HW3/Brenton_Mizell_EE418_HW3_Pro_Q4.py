#a)
""" A can easily depict the message for a number of reasons. Firstly because the english alphabet is
numbered 0-25 there are only 26 distinct possibilities because each number is encrypted seperately
This makes it very eaasy to brute force this attack by comparing the public key to the cyphertext. 
Because there are only 26 possible characters for each number it is easy to break. You will need additional
protocals and encrypting to ensure a more "secure" system


"""
#b)
# Given data for the RSA cryptosystem and the ciphertext
n = 18721
b = 25
ciphertext = [365, 0, 4845, 14930, 2608, 2608, 0]

# Encrypting all possible plaintexts (0 to 25) using the public key
encrypted_values = {pow(i, b, n): i for i in range(26)}

# Decrypting the ciphertext
decrypted_message_numbers = [encrypted_values[c] if c in encrypted_values else '?' for c in ciphertext]
decrypted_message = ''.join(chr(i + 65) for i in decrypted_message_numbers)  # Converting numbers to letters

print(decrypted_message, decrypted_message_numbers)