def shift_cipher_decrypt(ciphertext, K):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine if character is upper or lowercase and then decrypt
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            decrypted_text += chr((ord(char) - base - K) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text

# Read the ciphertext from the file
with open('sampleFICT.txt', 'r') as f:
    ciphertext = f.read()

# Decrypt the ciphertext using the shift key K = 15
K = 15
plaintext = shift_cipher_decrypt(ciphertext, K)

# Write the decrypted text to a file named "FirstName LastName shift output.txt"
with open('Brenton_Mizell_shift_output.txt', 'w') as f:
    f.write(plaintext)

# Print the 30th to 39th ciphertext characters and their corresponding plaintext
print("Ciphertext (30th to 39th characters):", ciphertext[29:39])
print("Plaintext (30th to 39th characters):", plaintext[29:39])
