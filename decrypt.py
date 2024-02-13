from matrix_handler import *
def decrypt(d_str: str,key):
    pass
    ex = convert_str_to_matrix(d_str,key)
    ex = transpose_2(ex)

    ex = flatten_matrix(ex)
    return ex
