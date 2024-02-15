def mod_inverse(b, m):
    g, x, _ = extended_gcd(b, m)
    if g == 1:
        return x % m
    else:
        return None

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def decrypt_elgamal(c1, c2, p, a):
    inverse_c1 = mod_inverse(pow(c1, a, p), p)
    return (c2 * inverse_c1) % p

#Decode numeric block to a three-letter string
def decode_numeric_block(num):
    letters = []
    for _ in range(3):
        num, value = divmod(num, 26)
        letters.append(chr(value + 65))  # Convert to uppercase alphabet (A=0, B=1, ..., Z=25)
    return ''.join(reversed(letters))

#decrypt and decode ElGamal ciphertext
def decrypt_and_decode_elgamal(ciphertext_pairs, p, a):
    decrypted_message = ""
    for c1, c2 in ciphertext_pairs:
        # Decrypt
        decrypted_numeric = decrypt_elgamal(c1, c2, p, a)
        # Decode
        decrypted_text = decode_numeric_block(decrypted_numeric)
        decrypted_message += decrypted_text
    return decrypted_message

# ElGamal parameters
alpha = 5
beta = 18074
p = 31847
private_key_a = 7899

# ElGamal ciphertext (pairs)
ciphertext_pairs = [
    (3781, 14409), (31552, 3930), (27214, 15442), (5809, 30274),
    (5400, 31486), (19936, 721), (27765, 29284), (29820, 7710),
    (31590, 26470), (3781, 14409), (15898, 30844), (19048, 12914),
    (16160, 3129), (301, 17252), (24689, 7776), (28856, 15720),
    (30555, 24611), (20501, 2922), (13659, 5015), (5740, 31233),
    (1616, 14170), (4294, 2307), (2320, 29174), (3036, 20132),
    (14130, 22010), (25910, 19663), (19557, 10145), (18899, 27609),
    (26004, 25056), (5400, 31486), (9526, 3019), (12962, 15189),
    (29538, 5408), (3149, 7400), (9396, 3058), (27149, 20535),
    (1777, 8737), (26117, 14251), (7129, 18195), (25302, 10248),
    (23258, 3468), (26052, 20545), (21958, 5713), (346, 31194),
    (8836, 25898), (8794, 17358), (1777, 8737), (25038, 12483),
    (10422, 5552), (1777, 8737), (3780, 16360), (11685, 133),
    (25115, 10840), (14130, 22010), (16081, 16414), (28580, 20845),
    (23418, 22058), (24139, 9580), (173, 17075), (2016, 18131),
    (19886, 22344), (21600, 25505), (27119, 19921), (23312, 16906),
    (21563, 7891), (28250, 21321), (28327, 19237), (15313, 28649),
    (24271, 8480), (26592, 25457), (9660, 7939), (10267, 20623),
    (30499, 14423), (5839, 24179), (12846, 6598), (9284, 27858),
    (24875, 17641), (1777, 8737), (18825, 19671), (31306, 11929),
    (3576, 4630), (26664, 27572), (27011, 29164), (22763, 8992),
    (3149, 7400), (8951, 29435), (2059, 3977), (16258, 30341),
    (21541, 19004), (5865, 29526), (10536, 6941), (1777, 8737),
    (17561, 11884), (2209, 6107), (10422, 5552), (19371, 21005),
    (26521, 5803), (14884, 14280), (4328, 8635), (28250, 21321),
    (28327, 19237), (15313, 28649)
]

# Decrypt and decode the message and print it
decrypted_and_decoded_message = decrypt_and_decode_elgamal(ciphertext_pairs, p, private_key_a)
print(decrypted_and_decoded_message)

"""
Output:
    SHESTANDSUPINTHEGARDENWHERESHEHASBEENWORKINGANDLOOKSINTOTHEDISTANCESHEHASSENSEDACHANGE
    INTHEWEATHERTHEREISANOTHERGUSTOFWINDABUCKLEOFNOISEINTHEAIRANDTHETALLCYPRESSESSWAYSHE
    TURNSANDMOVESUPHILLTOWARDSTHEHOUSECLIMBINGOVERALOWWALLFEELINGTHEFIRSTDROPSOFRAINONHER
    BAREARMSSHECROSSESTHELOGGIAANDQUICKLYENTERSTHEHOUSE
"""