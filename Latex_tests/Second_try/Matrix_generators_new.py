from Header import *
from Checkers import *
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


def gen_UniUpperM(size, help_func):
    return sp.Matrix(size, size, help_func)


def gen_OneZeroUpperM(size, help_func):
    return sp.Matrix(size, size, help_func)


def gen_InvertibleM(size, help_func):
    left = gen_OneZeroUpperM(size, help_func).T
    right = gen_OneZeroUpperM(size, help_func)
    return left * right


def gen_BoundedInvertibleM(size, bound, help_func):
    result = gen_InvertibleM(size, help_func)
    while checker_isBounded(bound, result.inv()) is False or checker_isBounded(bound, result) is False:
        result = gen_InvertibleM(size, help_func)
    return result


def gen_RankedM(rows, columns, rank, random):
    result = sp.Matrix(rows, columns, lambda x, y: random())
    while result.rank() != rank:
        result = sp.Matrix(rows, columns, lambda x, y: random())
    return result
