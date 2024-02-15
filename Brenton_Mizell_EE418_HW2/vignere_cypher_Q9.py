import string

# Compute the Index of Coincidence (IoC) for a given text
def index_of_coincidence(text):
    N = len(text)
    # Count the frequency of each uppercase letter in the text
    freqs = [text.count(letter) for letter in string.ascii_uppercase]
    # Calculate the IoC value
    IoC = sum([f*(f-1) for f in freqs]) / (N*(N-1))
    return IoC

# Compute the average IoC for a given key length
def average_ioc_for_key_length(ciphertext, key_length):
    iocs = []
    # Split the ciphertext into segments based on the key length and compute IoC for each segment
    for i in range(key_length):
        segment = ciphertext[i::key_length]
        iocs.append(index_of_coincidence(segment))
    # Return the average IoC for all segments
    return sum(iocs) / key_length

# Determine the probable key lengths based on average IoC values
def probable_key_lengths(ciphertext, max_key_length=10):
    avg_iocs = [(key_length, average_ioc_for_key_length(ciphertext, key_length))
                for key_length in range(1, max_key_length + 1)]
    # Sort the key lengths based on their average IoC values in descending order
    avg_iocs.sort(key=lambda x: x[1], reverse=True)
    return avg_iocs

# Compute the most likely shift for a given text based on English letter frequencies
def compute_shift(text):
    # Define the standard English letter frequencies
    english_freqs = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074
    ]

    max_corr = -1.0
    best_shift = 0
    # Compute a correlation score for each possible shift
    for i in range(26):
        shifted_freqs = [text.count(chr((j+i)%26 + 65)) / len(text) for j in range(26)]
        corr = sum([english_freqs[j] * shifted_freqs[j] for j in range(26)])
        # Find the shift with the highest correlation to English frequencies
        if corr > max_corr:
            max_corr = corr
            best_shift = i
    return best_shift

# Decrypt a Vigenère ciphertext using a given key
def vigenere_decrypt(text, key):
    decrypted = ""
    for i, char in enumerate(text):
        # Decrypt only alphabetic characters
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypted += char
    return decrypted

def main():
    # Take user input for the ciphertext and convert to uppercase
    ciphertext = input("Enter the ciphertext: ").upper()
    # Rank the probable key lengths based on their average IoC values
    ranked_key_lengths = probable_key_lengths(ciphertext)

    print("Most likely key lengths (ranked):")
    for key_length, ioc in ranked_key_lengths:
        print(f"Key length: {key_length}, IoC: {ioc:.4f}")

    # Let the user choose a key length
    key_length = int(input("Choose one of the key lengths above: "))

    key = ""
    # Compute the probable key based on the chosen key length
    for i in range(key_length):
        sequence = ciphertext[i::key_length]
        shift = compute_shift(sequence)
        key += chr(shift + 65)

    print("The probable key is:", key)
    
    # Decrypt the ciphertext using the probable key
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("Deciphered text:", decrypted_text)

# Execute the main function when the script is run
if __name__ == "__main__":
    main()

"""
a)
KTSVFVMHMCHJUBFDYLMGRWZXNHMVDSVNUBJOJULFZNAQILXSXOJYOROEFJTDXWCNERALABFMLVJFFSEFVXLUJQBORDKMLFBVGYNXLSNJQDWARDXQHAMBRHUPGTYXVVUYXEXHAQJVMLJEZFZBVQPBYPQMPBCUJHBUDSKQFOTVTFGKYXNPDWXJQYVOWLJDUJNJHBUUFUPFOFUTCLWKFJWMKDMOLYNZSQBVBJJHWEEQHLLWTWTORYZXXDYZXOVFPMIHXBMEHSSHZRZKXORYWAPSTZNURNUEFVYPWTRZAQBIWPLBQXLLVUNARFVNNJWHFZCBUYVOBVYVWJVMTNOWFJLVVYVVFGFZRXDXAXIRQTNTVHBAJRZZOBFZSCJHXAQJVXBMEHSPWUUZZRPQNUCPPDTXTWNUCJPFANUKTBPIWXDJTXYANSODPWFAUSRDDGSN
"""

"""
b)
KSQRAUHSQGGBFDQSXOIXMRWCSYFWAAPPOSELGYQGWZGLDCXVFZZIHLCAXILVRTEWGSJPFLWWCWUXAJOWNEFKGHTMUOVLHIUVBYQGLLRETIEDWETEFVHSQVSUREAEKZIXQEEVBRFLWWCHQVKVTETIWHFETXZLGPBEJHHPMRVLEFMPKAOEUSFACHTMUOHSQPSDGZRRSAICQEFKCQZELBFPEKGKSYFMLSSETIEHRPOIFAFPETWJHEAXZLCAURAVBDAJEHBVURVYSBGMJLGETELAVPKWZVIWPHWJZLDILOSNMYKLGHTMUOWXBIDAVPYXGAVPEIHHFLFMGU
"""

"""
c)
GGAMGHUMEDWXUFFAOQLYYSALSHUMEDDXPDVUMAKREIKLAZFEMJQHKKBYKQKYSHVRQFATXMMSFBAHZBXHXHQCGOLERXXTOPPYFBMFRPNVFPZULZWTFQBIYQTHLRTVCAVSKFTWKZFLJGKNXNUVFALYLFRSIXVUHOVJWHVLGOLOHSXTPQFVMQGHVNRQRKTQLXEVGPRCLZBKXWGZEFWFHLVPREVJRQRNWJPHAVDZBSESFFGPVZMTQPVERTHFBHEACKNSFEBXSUEOLWAAZWEEJFPHSSHWMIJJFJYKIYECCILZPEBSGAWARZATXXXJFVBMZUWJGWCKALSMMYERMPGOHFWTRDVQNYNQMBIPMKRZZQLNRIJBPYFBMTKGCMUPJMELSGKQUTZFAJQHGIILZNNYMCUQRHKQQUPDKQJLHWGJWHGPVUATXNVXOMYLTQGYEIKLALCQGYLDWDUAOQZTEAJXFILQGYLTUXZLATXRIIJLQZHZWYIRJKVXBQLTJRTVCAHZTQCHKPUHCQVMECIBQKYMLYMRCIYFATKTYVJQULOULYSGALSJYKIYSVTXCOFMWFTIKKTAVUGHVTCPVUNOKDTIQDEHWTBHGDOMYLEUMDVPPDVUNRKTQIJBCLUMGITPRBETLFATHHQCGOLBTXXIJOBBNTFFGWKKRZSUDJXWGYEPAULMFDOYRZHZWHSAQPFBZOHRTJVBEZHFUQIIEEYLFBTWOXPTBYSPPFVXKQBAOQFFXWGJNAPOTQPNCAIHUOXIGDOMHALDBEISUZULTQLTJIJBCYLEXSXBGQUVKEYTVQTBNRPZZRSSGOAJYKIYSHAPGLTEHKXTPFACVXOJWDNSVUNOTWIUWIYFJAGXXGWZGLKBKTFAGJFPUBNWIBCQULTMMNGHVERILEMPRDYKOLPZZNRIGDRYMMVYSGKWNAPAG
"""