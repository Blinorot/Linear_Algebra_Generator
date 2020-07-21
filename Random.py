# NZ for non-zero, WZ for with-zero


class Random(object):
    def __init__(self, max_value, first_value, second_value):
        self.max_value = max_value
        self.first_value = first_value
        self.second_value = second_value

    def Sign():
        return -1 if np.random.randint(2) == 0 else 1

    def BoundedWZ():
        return randomSign() * np.random.randint(self.max_value)

    def BoundedNZ():
        result = self.BoundedWZ(self.max_value)
        while result == 0:
            result = self.BoundedWZ(self.max_value)
        return result

    def BoundedNonEqualPair():
        first_elem = np.random.randint(first_value)
        second_elem = np.random.randint(second_value)
        while second_elem == first_elem:
            second_elem = np.random.randint(second_value)
        return first_elem, second_elem
