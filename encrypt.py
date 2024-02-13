from matrix_handler import *

def encrypt(in_str: str, in_key) -> str:
    # input: string from a file
    # output: encrypted string

    output_str = ""

    if is_int(in_key):
        str_matrix = convert_str_to_matrix(in_str, in_key) #multi-dim list represents a matrix
        str_matrix_T = transpose_2(str_matrix) # Transposed string matrix
        flat_matrix = flatten_matrix(str_matrix_T)
    else:
        print("Key is not an int.")

    return flat_matrix