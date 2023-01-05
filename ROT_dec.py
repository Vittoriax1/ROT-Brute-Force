import enchant

def rot_decrypt(text):
    # Try all possible rotation factors
    for i in range(26):
        # Create a mapping of the alphabet to the rotated alphabet
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rotated_alphabet = alphabet[i:] + alphabet[:i]
        mapping = {c: r for c, r in zip(alphabet, rotated_alphabet)}

        # Decrypt the text by replacing each letter with the corresponding letter in the rotated alphabet
        decrypted_text = ""
        for c in text:
            decrypted_text += mapping.get(c.upper(), c)

        # Check if the decrypted text is valid English
        english_dict = enchant.Dict("en_US")
        if all(english_dict.check(word) for word in decrypted_text.split()):
            # Highlight the correct decoding
            print(f"\033[1mROT-{i}: {decrypted_text}\033[0m")
        else:
            # Print the decoding as normal
            print(f"ROT-{i}: {decrypted_text}")

# Get the ciphertext from the user
text = input("Enter the ciphertext: ")

# Decrypt the ciphertext
rot_decrypt(text)
