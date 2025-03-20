# Caesar Cipher Encryption and Decryption

## Overview
This Python script implements a simple Caesar cipher for encrypting and decrypting text. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a fixed number of places in the alphabet.

## Features
- Encrypt text using a specified shift value or a randomly generated shift value.
- Decrypt text using a known shift value.
- Brute-force decryption option to display all possible shifts.
- Recursive functionality allowing users to continue encrypting and decrypting.

## Prerequisites
This script requires Python 3.x to run.

## How to Use
1. Run the script:
   ```sh
   python script.py
   ```
2. Choose an operation:
   - Press `1` to encrypt text.
   - Press `2` to decrypt text.
3. Follow the prompts:
   - For encryption, enter a shift value or opt for a random shift.
   - For decryption, enter a known shift value or view all possible shifts.
4. Choose whether to continue or exit the program.

## Example
### Encryption
Input:
```
Choose operation:
1. Encrypt 2. Decrypt: 1
Enter the text to be encrypted: hello
Random shift value? (y/n): y
Shift: 5
Encrypted Text: mjqqt
```

### Decryption
Input:
```
Choose operation:
1. Encrypt 2. Decrypt: 2
Enter the text to be decrypted: mjqqt
Enter the shift value: y
Enter the shift value: 5
Decrypted Text: hello
```

## Limitations
- Only works with alphabetic characters (A-Z, a-z).
- Does not preserve spaces, punctuation, or special characters.

## License
This project is open-source and free to use under the MIT License.

## Author
Your Name

