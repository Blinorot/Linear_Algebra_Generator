def checker_isBounded(bound, matrix):
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            if matrix[i, j] > bound:
                return False
    return True
