def decrypt(cipher, ciphertext):
    return encrypt(inverse_key(cipher), ciphertext)

def encrypt(cipher, plaintext):
    plaintext = "".join(plaintext.split(" ")).upper()
    ciphertext = ""
    for pad in range(0, len(plaintext)%len(cipher)*-1%len(cipher)):
        plaintext += "X"
    for offset in range(0, len(plaintext), len(cipher)):
        for element in [a-1 for a in cipher]:
            ciphertext += plaintext[offset+element]

    return ciphertext

def inverse_key(cipher):
    inverse = []
    for position in range(min(cipher),max(cipher)+1,1):
        inverse.append(cipher.index(position)+1)
    return inverse

cipher = [4,1,6,2,7,3,8,5]

ciphertext = "T G E E M N E L N N T D R O E O A A H D O E T C S H A E I R L M"

plaintext = decrypt(cipher,ciphertext)
print(plaintext)

# Decrypted Message: GENTLEMENDONOTREADEACHOTHERSMAIL