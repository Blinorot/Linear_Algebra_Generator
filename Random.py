# NZ for non-zero, WZ for with-zero


class Random(object):
    seed = 0

    def __init__(self, min_value, max_value):
        np.random.seed(Random.seed)
        self.max_value = max_value
        self.first_value = first_value
        self.second_value = second_value

    def Bool(self):
        return np.random.randint(2)

    def Sign(self):
        return -1 if np.random.randint(2) == 0 else 1

    def BoundedWZ(self):
        return randomSign() * np.random.randint(self.max_value)

    def BoundedNZ(self):
        result = self.BoundedWZ(self.max_value)
        while result == 0:
            result = self.BoundedWZ(self.max_value)
        return result

    def BoundedNonEqualPair(self):
        first_elem = np.random.randint(first_value)
        second_elem = np.random.randint(second_value)
        while second_elem == first_elem:
            second_elem = np.random.randint(second_value)
        return first_elem, second_elem

    def MatrixWZ(self, row, column):
        result = sp.Matrix(row, column, lambda i, j: self.BoundedWZ())
        return result

    def MatrixNZ(self, row, column):
        result = sp.Matrix(row, column, lambda i, j: self.BoundedNZ())
        return result
