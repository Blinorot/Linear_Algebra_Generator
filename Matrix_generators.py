# M for matrix, NZ for non-zero, WZ for with-zero


def gen_FirstElementaryM(size, value, row, column):
    result = sp.eye(size)
    result[row, column] = value
    return result


def gen_SecondElementaryM(size, row, column):
    result = sp.eye(size)
    result[row, row] = 0
    result[row, column] = 1
    result[column, column] = 0
    result[column, row] = 1
    return result


def gen_ThirdElementaryM(size, value, index):
    result = sp.eye(size)
    result[index, index] = value
    return result


def gen_RandomFirstOrSecondElementaryM(size, random):
    flag = np.random.randint(4)
    row, column = random.BoundedNonEqualPair()
    if flag != 0:
        value = random.BoundedNZ()
        return gen_FirstElementaryM(size, value, row, column)
    else:
        return gen_SecondElementaryM(size, row, column)


def gen_PermutationM(size):
    result = sp.zeros(size, size)
    row = 0
    column = 0
    permutation = np.random.permutation(size)
    while (row < size):
        column = permutation[size]
        result[row, column] = 1
        row += 1
    return result


def gen_UniUpperWZM(size, help_func):
    return sp.matrix(size, size, help_func)


def gen_OneZeroUpperWZM(size, help_func):
    return sp.Matrix(size, size, help_func)


def gen_UniUpperNZM(size, help_func):
    return sp.matrix(size, size, help_func)


def gen_OneZeroUpperNZM(size, help_func):
    return sp.Matrix(size, size, help_func)


def gen_InvertibleM(size, random):
    left = gen_OneZeroUpperNZM(size, random).T
    right = gen_OneZeroUpperNZM(size, random)
    return left * right


def gen_BoundedInvertibleM(size, bound, random):
    result = gen_InveribleM(size, random)
    while checker_isBounded(bound, result.inv()) == False:
        result = gen_InvertibleM(size, random)
    return result


def gen_FullRankWZM(row, column, random):
    result = random.MatrixWZ(row, column)
    while result.rank() < min(row, column):
        result = random.MatrixWZ(row, column)
    return result


def gen_FullRankNZM(row, column, random):
    result = random.MatrixNZ(row, column)
    while result.rank() < min(row, column):
        result = random.MatrixNZ(row, column)
    return result
