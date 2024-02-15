#1. The program takes in the cypher text
#2. The program takes in the cypher text to plain text known
#3. THe program will use the English level frequencies of letters and the given cypher-plaitext letters
#   and will create three initial decoding options where the most common cypher letter is replaced with e, a, and t
#4. The user will decide (using intuition which one of the initial decoded messages looks the best)
#5. The program will ask the user if the message is correct, if no it will ask for a new/updated cypher-plain letter
#6. The program will indicate which Cypher text letters have not been mapped by keeping them Capitalized
#   and will also show the current mapping of cypher to plain
#7. The user will reiterate until the decoded message is correct
#8. In this case the user will use the context given to try and infer the words, aiding in the decryption



def substitution_cipher_decrypt(ciphertext, known_mappings, freq_char):
    # English letter frequencies in descending order
    freq_order = 'etaoinshrdlcumwfgypbvkjxqz'
    
    # Create a mapping of ciphertext to plaintext based on known mappings
    cipher_map = dict(known_mappings)
    
    # Identify the most frequent unmapped letter in the ciphertext (excluding space)
    most_common_unmapped = sorted([(char, ciphertext.count(char)) for char in set(ciphertext) if char not in cipher_map and char != ' '], key=lambda x: x[1], reverse=True)[0][0]
    
    # Map the most frequent unmapped letter to the given freq_char
    cipher_map[most_common_unmapped] = freq_char
    
    # Decrypt the ciphertext using the mappings
    plaintext = ''.join(cipher_map[c] if c in cipher_map else c for c in ciphertext)
    
    return plaintext, cipher_map

def main():
    # Input the ciphertext
    ciphertext = input("Enter the ciphertext: ").upper()

    # Input known mappings
    known_mappings = {}
    while True:
        cipher_char = input("Enter ciphertext character (or 'done' to finish): ").upper()
        if cipher_char == 'DONE':
            break
        plain_char = input(f"Enter plaintext for {cipher_char}: ").lower()
        known_mappings[cipher_char] = plain_char

    # Decrypt using known mappings and the three most frequent English letters
    options = {}
    for index, freq_char in enumerate(['e', 't', 'a']):
        decrypted, current_mappings = substitution_cipher_decrypt(ciphertext, known_mappings, freq_char)
        
        print(f"\nOption {index + 1} (Using '{freq_char}' for most frequent unmapped character):")
        print("Current Mappings:")
        for cipher, plain in current_mappings.items():
            print(f"{cipher} -> {plain}")
        print("\nDecrypted text:\n", decrypted)
        options[str(index + 1)] = (decrypted, current_mappings)

    # Let user select the best decryption
    choice = input("\nChoose the best option (1/2/3): ")
    decrypted, current_mappings = options[choice]

    # Continue with the program as previously described
    while True:
        user_feedback = input("\nIs the message good? (yes/no): ").lower()
        if user_feedback == 'yes':
            break
        else:
            # If not good, allow user to provide more known mappings
            cipher_char = input("Enter incorrect ciphertext character: ").upper()
            plain_char = input(f"Enter correct plaintext for {cipher_char}: ").lower()
            known_mappings[cipher_char] = plain_char
            decrypted, current_mappings = substitution_cipher_decrypt(ciphertext, known_mappings, 'e')
            print("\nOriginal Ciphertext:\n", ciphertext)
            print("\nCurrent Mappings:")
            for cipher, plain in current_mappings.items():
                print(f"{cipher} -> {plain}")
            print("\nDecrypted text:\n", decrypted)

if __name__ == "__main__":
    main()
