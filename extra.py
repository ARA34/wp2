import sys
from pathlib import Path
from content_handler import *
from encrypt import *
from decrypt import *


current_path = Path(".").resolve()
# original.txt -> encrypt.txt -> decrypt.txt


def main():
    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    key = sys.argv[4]

    if command == "-e":
        # encrypt
        pass
    elif command == "-d":
        # decrypt

        pass
    else:
        print("Wrong input")




if __name__ == "__main__":
    main()
