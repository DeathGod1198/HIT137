import re

def separate_string(s):
    # Separate numbers and letters using regex
    num_str = ''.join(re.findall(r'\d', s))
    letter_str = ''.join(re.findall(r'[A-Za-z]', s))
    
    return num_str, letter_str

def convert_even_numbers_to_ascii(num_str):
    # Convert even numbers to their ASCII code values
    ascii_codes = [ord(ch) for ch in num_str if int(ch) % 2 == 0]
    
    return ascii_codes

def convert_uppercase_letters_to_ascii(letter_str):
    # Convert uppercase letters to their ASCII code values
    ascii_codes = [ord(ch) for ch in letter_str if ch.isupper()]
    
    return ascii_codes


# Example scenario
input_string = input("Enter a long string that contains both numbers and letters:")
num_str, letter_str = separate_string(input_string)

print(f"Number String: {num_str}")
print(f"Letter String: {letter_str}")

even_number_ascii_codes = convert_even_numbers_to_ascii(num_str)
print(f"Even Number ASCII Codes: {even_number_ascii_codes}")

uppercase_letter_ascii_codes = convert_uppercase_letters_to_ascii(letter_str)
print(f"Uppercase Letter ASCII Codes: {uppercase_letter_ascii_codes}")


from collections import Counter

# Function to decrypt cryptogram using a shift key
def decrypt_cryptogram(cryptogram, s):
    decrypted_message = []
    
    for char in cryptogram:
        if char.isalpha():  # Check if the character is a letter
            if char.isupper():
                decrypted_message.append(chr((ord(char) - s - 65) % 26 + 65))  # Uppercase letter decryption
            else:
                decrypted_message.append(chr((ord(char) - s - 97) % 26 + 97))  # Lowercase letter decryption
        else:
            decrypted_message.append(char)  # Keep spaces and punctuation unchanged
    
    return ''.join(decrypted_message)

# Function to analyze letter frequency and estimate the shift key
def estimate_shift_key(cryptogram):
    # Remove non-alphabetic characters and convert to uppercase for analysis
    letters_only = ''.join([char for char in cryptogram if char.isalpha()]).upper()

    # Count the frequency of each letter in the cryptogram
    letter_counts = Counter(letters_only)
    
    # Find the most frequent letter in the cryptogram
    most_common_letter, _ = letter_counts.most_common(1)[0]

    # The most common letter in English is 'E', so we calculate the shift
    shift_key = (ord(most_common_letter) - ord('E')) % 26

    return shift_key

# Example cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYOBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Estimate the shift key
shift_key = estimate_shift_key(cryptogram)

# Decrypt the cryptogram using the estimated shift key
decrypted_message = decrypt_cryptogram(cryptogram, shift_key)

# Display the results
print(f"Estimated Shift Key: {shift_key}")
print(f"Decrypted Message: {decrypted_message}")
