import numpy as np

# Hill cipher encryption function
def hill_cipher_encrypt(block, key):
    # Convert the input block to a matrix format
    block_matrix = np.array([int(bit) for bit in block]).reshape((4, 4))
    # Perform matrix multiplication in mod 2
    encrypted_matrix = np.mod(np.dot(block_matrix, key), 2)
    # Convert the matrix back to a string
    encrypted_block = ''.join(str(bit) for bit in encrypted_matrix.flatten())
    return encrypted_block

# Vigenère cipher encryption function
def vigenere_cipher_encrypt(block, key):
    # XOR the block with the key (since all operations are in mod 2, this is equivalent to Vigenère cipher)
    encrypted_block = ''.join(str(int(block_bit) ^ int(key_bit)) for block_bit, key_bit in zip(block, key))
    return encrypted_block

# CBC-MAC function
def cbc_mac(message, iv, hill_key, vigenere_key):
    # Split the message into blocks of size t
    t = 16
    blocks = [message[i:i+t] for i in range(0, len(message), t)]
    
    # Initial vector
    c = iv
    
    # Process each block
    for i, block in enumerate(blocks, 1):
        # XOR with the previous encrypted block
        block = ''.join(str(int(block[j]) ^ int(c[j])) for j in range(len(block)))
        
        # Encrypt the block based on whether the index is even or odd
        if i % 2 == 0:  # Hill cipher for even indices
            c = hill_cipher_encrypt(block, hill_key)
        else:           # Vigenère cipher for odd indices
            c = vigenere_cipher_encrypt(block, vigenere_key)
    
    # The last block is the CBC-MAC
    return c

# Define the keys and IV
hill_key = np.array([[0, 1, 0, 0],
                     [1, 0, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]])
vigenere_key = "1001001111001001"
iv = "1010000011111010"

# Message
message = "100110010011100011000101000111101100111110101010010110110101100001101110010101111100000010001001"

# Calculate the CBC-MAC
cbc_mac_value = cbc_mac(message, iv, hill_key, vigenere_key)
print(cbc_mac_value)
#
