
def is_int(val):
        # from Lab 8
        if type(val).__name__ == "str" and "." in val:
            return False
        try:
            int(val)
            return True
        except ValueError:
            return False
        

# switching rows and columns
#[[a,b],[c,d]] --> 2x2 matrix
# [[1,2]] --> 1x2 matrix 
# [[1],[2]] --> 2x1 matrix

m_n = [["a","b","c"],["d","e","f"]] # [["a","d"],["b","e"],["c","f"]]
m_n = [["a","d"],["b","e"],["c","f"]]
# 2x3
# [a b c] --> [a d]
# [d e f]     [b e]
#             [c f]

# 3x2
# [a d]     [a b c]
# [b e] --> [d e f]
# [c f]

def calc_dim(matrix: list):
    return len(matrix), len(matrix[0])


def transpose(matrix: list) -> list:
    # input: multi-dim list matrix
    # output: multi-dim list output_m
    output_m = []
    for i in range(len(matrix[0])):
        output_m.append([matrix[0][i]])
        for j in range(1, len(matrix)):
            output_m[i].append(matrix[j][i])
    print(f"output_m: {output_m}")
    return output_m

def transpose_2(matrix:list):
    output_m = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return output_m






def convert_str_to_matrix(matrix_str: str, key: int) -> list:
    # input 1: int key
    # input 2: str matrix_str
    # output: mutli-dim list output_m
    output_m = []
    n_matrix_str = matrix_str
    # ex. "Hello_world"

    iter_times = len(matrix_str)//key
    for i in range(iter_times):
        output_m.append(n_matrix_str[:key])
        n_matrix_str = n_matrix_str[key:]
    rem = n_matrix_str
    for s in range(key - len(rem)):
        n_matrix_str += "_"
    output_m.append(n_matrix_str)

    for sect in range(len(output_m)):
        output_m[sect] = [*output_m[sect]]
    return output_m


def flatten_matrix(mn_matrix: list) -> str:
    output = ""
    for row in mn_matrix:
        output += "".join(row)
    return output


def print_matrix(mn_matrix: list) -> str:
    output = ""
    for row in mn_matrix:
        output += str(row) + "\n" 
    print (output)

# ex = "This_is_a_random_message"
# matrix_ex = convert_str_to_matrix(ex,5)
# print("OG matrix:")
# print_matrix(matrix_ex)

# print("\n\n")

# matrix_T = transpose(matrix_ex)
# m,n = calc_dim(matrix_T)
# print("Transposed Once:")
# print_matrix(matrix_T)

# print(f"Flat: {flatten_matrix(matrix_T)}")


# # tranposing twice is not working
# new_str = ""
# for sub in matrix_T:
#     new_str += "".join(sub)
# new_str_matrix = convert_str_to_matrix(new_str,5)
# print(f"New orignal: {new_str_matrix}")


# matrix_T_2 = transpose(new_str_matrix)
# m,n = calc_dim(matrix_T_2)

#print(transpose(m_n))


# m,n = calc_dim(m_n)
# print(f"The matrix is {m}x{n}")
    
# ex. key = 5
    
# ex = "Hello this is a message"
# ex = convert_str_to_matrix(ex,5)


# print_matrix(transpose_2(ex))
# ex = transpose(ex)
# ex = flatten_matrix(ex)

# de = convert_str_to_matrix(ex,3)
# print_matrix(de)
# de = transpose(de)
# de = list(map(lambda r: r[:-1], de))
# print_matrix(de)
