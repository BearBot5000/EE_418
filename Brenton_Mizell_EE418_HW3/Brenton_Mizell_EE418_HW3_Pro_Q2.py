from sympy import mod_inverse

#a)
# Given values
n = 31313
b = 4913

# Function to factor n using a brute-force approach
def factor_n(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

# Factoring n
p, q = factor_n(n)

# Compute phi(n)
phi_n = (p - 1) * (q - 1)

# Compute RSA private key a
a = mod_inverse(b, phi_n)

#b)
def square_and_multiply(c, a, n):
    """Computes c^a mod n using the Square-and-Multiply algorithm."""
    e = 1
    binary_a = bin(a)[2:]  # Convert exponent 'a' to binary representation

    for i in binary_a:
        e = (e * e) % n
        if i == '1':
            e = (e * c) % n

    return e

#c)
def decode_block(encoded_block):
    """Decodes an encoded block back into its three-letter string representation."""
    characters = []
    for _ in range(3):
        # Find the character corresponding to the remainder
        char_code = encoded_block % 26
        characters.append(chr(char_code + 65))  # Convert to alphabet
        encoded_block //= 26
    return ''.join(reversed(characters))

# Ciphertext blocks from Table 1
ciphertext_blocks = [
    6340, 8309, 14010, 8936, 27358, 25023, 16481, 25809,
    23614, 7135, 24996, 30590, 27570, 26486, 30388, 9395,
    27584, 14999, 4517, 12146, 29421, 26439, 1606, 17881,
    25774, 7647, 23901, 7372, 25774, 18436, 12056, 13547,
    7908, 8635, 2149, 1908, 22076, 7372, 8686, 1304,
    4082, 11803, 5314, 107, 7359, 22470, 7372, 22827,
    15698, 30317, 4685, 14696, 30388, 8671, 29956, 15705,
    1417, 26905, 25809, 28347, 26277, 7897, 20240, 21519,
    12437, 1108, 27106, 18743, 24144, 10685, 25234, 30155,
    23005, 8267, 9917, 7994, 9694, 2149, 10042, 27705,
    15930, 29748, 8635, 23645, 11738, 24591, 20240, 27212,
    27486, 9741, 2149, 29329, 2149, 5501, 14015, 30155,
    18154, 22319, 27705, 20321, 23254, 13624, 3249, 5443,
    2149, 16975, 16087, 14600, 27705, 19386, 7325, 26277,
    19554, 23614, 7553, 4734, 8091, 23973, 14015, 107,
    3183, 17347, 25234, 4595, 21498, 6360, 19837, 8463,
    6000, 31280, 29413, 2066, 369, 23204, 8425, 7792,
    25973, 4477, 30989
]

# Decrypt and decode each block
plaintext_blocks = []

for c in ciphertext_blocks:
    # Decrypt the ciphertext block
    decrypted_block = square_and_multiply(c, a, n)
    # Decode the decrypted block
    decoded_block = decode_block(decrypted_block)
    plaintext_blocks.append(decoded_block)

# Join the plaintext blocks into a single string
decrypted_message = ''.join(plaintext_blocks)
print(decrypted_message)  # Display the decrypted message
