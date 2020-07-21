# M for matrix, NZ for non-zero, WZ for with-zero


def gen_FirstElementaryMV(size, max_value=5, value=randomNZ(max_value)):
    result = np.identity(size, dtype=int)
    index = [randomNonEqualPair(size, size)]
    result[index[0]][index[1]] = value
    return result


def gen_FirstElementaryM(size, max_value=5):
    return gen_FirstElementaryMV(size, randomNZ(max_value))


def gen_SecondElementaryMV(size, row, column):
    result = np.identity(size, dtype=int)
    result[row][row] = 0
    result[row][column] = 1
    result[column][column] = 0
    result[column][row] = 1
    return result


def gen_SecondElementaryM(size):
    row, column = randomNonEqualPair(size, size)
    return gen_SecondElementaryMV(size, row, column)


def gen_ThirdElementaryV(size, value):
    result = np.identity(size, dtype=int)
    index = np.random.randint(size)
    result[index][index] = value
    return result


def gen_PermutationM(size):
    result = np.zeroes((size, size), dtype=int)
    row = 0
    column = 0
    permutation = np.random.permutation(size)
    while (row < size):
        column = permutation(size)
        result[row][column] = 1
        row += 1
    return result
