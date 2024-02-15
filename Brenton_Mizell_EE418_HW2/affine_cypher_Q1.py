def affine_decrypt(Y, a, b):
    # Find the multiplicative inverse of a mod 26
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None
    
    m = 26  # For English alphabet
    a_inv = mod_inverse(a, m)
    
    if a_inv is None:
        raise ValueError(f"{a} has no multiplicative inverse modulo {m}")
    
    # Convert ciphertext into numbers (0-25) and decrypt
    plaintext = ""
    for letter in Y:
        if letter.isalpha():
            num = (a_inv * (ord(letter.upper()) - 65 - b)) % m
            plaintext += chr(num + 65)
        else:
            plaintext += letter
    
    return plaintext

def main():
    # Get user inputs
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    input_file_path = input("Enter the path of the file to decrypt: ")
    output_file_path = input("Enter the path to save the decrypted content: ")

    # Read the ciphertext from the file
    with open(input_file_path, 'r') as f:
        ciphertext = f.read()
    
    # Decrypt the content
    decrypted_content = affine_decrypt(ciphertext, a, b)

    # Write the decrypted content to the output file
    with open(output_file_path, 'w') as f:
        f.write(decrypted_content)

    print(f"Decryption complete! Check the file: {output_file_path}")

    # Extract the 30th to 39th characters (Python uses 0-based indexing)
    ciphertext_segment = ciphertext[29:39]

    # Decrypt the segment
    plaintext_segment = affine_decrypt(ciphertext_segment, a, b)

    # Print the results
    print(f"Ciphertext (30th to 39th characters): {ciphertext_segment}")
    print(f"Corresponding Plaintext: {plaintext_segment}")

if __name__ == "__main__":
    main()
