# Transposition Cipher Workout Project 2
# Alex Reyes Aranda
# areyesar@uci.edu

def scramble_message(input: str, key: int):
    # input: str input, int key
    # output: str output_str
    output_str = ""
    str_list = []
    iter_times = len(input)//key
    for i in range(iter_times):
        print(i)
        str_list.append(input[i:i+key])
        input = input[i+key:]
    str_list.append(input)
    output_str = "".join(str_list)
    return output_str
    ["Hello w", "orld"]
    # H

def str_to_matrix(input_list: str):
    # input: list input
    # output: multidimensional list representing matrix of axb
    output_matrix = []

    # [[1],[2]] is a 1x2 matrix with 2 entries
    # [[1,2],[3,4]] is a 2x2 matrix with 4 entries

    for i in range(len(input_list)):
        for j in range(len(i)):

    pass


def transpose():
    # input: multidimensional list representing matrix of mxn
    # output: mutlidimensional list representing matrix of nxm
    pass

[[],[]]

print(scramble_message("Hello world",7))

