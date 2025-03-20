# caesar_cipher_project/
# ├── README.md
# ├── cipher.py
# └─IU
# #     └── test_cipher.p
import random

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    user_choice = int(input("Choose operation: \n1. Encrypt 2. Decrypt: "))
    if user_choice == int(1):
        text = input("Enter the text to be encrypted: ")
        shift_choice = input("Random shift value? (y/n): ")
        if shift_choice == "y":
            shift = random.randint(1, 25)
            print(f"Shift: {shift} \n")
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted Text: {encrypted_text}")
        else:
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted Text: {encrypted_text}")
    elif user_choice == int(2):
        text = input("Enter the text to be dencrypted: ")
        shift_choice = input("Enter the shift value: \n1. Custom?(y/n)")
        if shift_choice == "y":
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted Text: {decrypted_text}")
        else:
            for i in range(1, 26):
                shift = i
                decrypted_text = decrypt(text, i)
                print(f"Shift: {i} \nDecrypted Text: {decrypted_text}")
    else:
        print("Invalid choice.")
        return
    
    #Quit the program or continue
    user_choice = input("Do you want to continue? (y/n): ")
    if user_choice == "y":
        main()
    else:
        return

if __name__ == "__main__":
    main()
