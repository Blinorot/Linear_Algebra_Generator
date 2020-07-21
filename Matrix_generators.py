# M for matrix, NZ for non-zero, WZ for with-zero


def gen_FirstElementaryM(size, value, first_index, second_index):
    result = sp.eye(size)
    result[first_index, second_index] = value
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


def gen_UniUpperM(size, random):
    result = sp.zeros(size)
    for row in range(size):
        for column in range(row):
            result[row, column] = 1 if row == column else random.max_value()
    return result


def genOneZeroUpperM(size, random):
    result = sp.eye(size)
    for row in range(size):
        for column in range(row):
            if row == column:
                result[row, column] = np.random.randint(2)
            else:
                result[row, column] = random.max_value()
    return result
