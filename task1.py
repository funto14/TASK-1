def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")

    # Input from user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (integer): "))

    # Encryption
    encrypted_message = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted_message)

    # Decryption
    decrypted_message = decrypt(encrypted_message, shift)
    print("\nDecrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
