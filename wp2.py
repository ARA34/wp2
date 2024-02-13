import sys
from pathlib import Path
from content_handler import *
from encrypt import *
from decrypt import *

# Transposition Cipher Workout Project 2
# Alex Reyes Aranda
# areyesar@uci.edu


CURRENT = Path(".").resolve()
# original.txt -> encrypt.txt -> decrypt.txt


def main():
    command = sys.argv[1]

    input_file = sys.argv[2]
    input_path = Path(CURRENT/input_file)

    output_file = sys.argv[3]
    output_path = Path(CURRENT/output_file)
    key = sys.argv[4]

    if command == "-e":
        # encrypt: python3 extra.py -e original_text.txt encrypted_text.txt 5
        # input: string from input file
        # ouput: string encrypt string into output file
        original_msg = get_info(input_path)
        e_message = encrypt(original_msg, int(key))
        store_info(output_path, e_message)
    elif command == "-d":
        # decrypt: python3 extra.py -d encrypted_text.txt decrypted_text.txt
        # input: string encrypted from input file
        # output: string decrypted into output file

        # TODO LATER
        encrypted_msg = get_info(input_path)
        d_message = decrypt(encrypted_msg, key)
        store_info(output_path, d_message)
    else:
        print("Wrong input")




if __name__ == "__main__":
    main()
