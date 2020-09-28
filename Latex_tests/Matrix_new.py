from Random_new import *
from Matrix_generators_new import *
from Header import *


class MatrixForm:
    __default_Random = Random(0, 1)

    @classmethod
    def reset_default_random(cls, min_value, max_value):
        cls.__default_Random = Random(min_value, max_value)

    def __init__(self, **flags):
        self.form = flags["form"]
        if flags.get("allow_zeros", False) is False:
            self.rand = flags.get("random", MatrixForm.__default_Random)
            self.rand.Filter(lambda x: x != 0)
        else:
            self.rand = flags.get("random", MatrixForm.__default_Random)

        # make generator with right form
        if (self.form == "FirstElementary"):
            assert "size" in flags, 'Size was not given'
            size = flags["size"]
            index_random = Random(0, size - 1)
            self.gen = partial(self.FirstElementaryForm,
                               index_random, size, flags)

        if (self.form == "Invertible"):
            assert "size" in flags, 'Size was not given'
            size = flags["size"]
            self.gen = partial(self.InvertibleForm, size, flags)

    def __call__(self):
        return self.gen()

    # Functions to make form
    def FirstElementaryForm(self, index_random, size, flags):
        row = flags.get("row", -1)
        column = flags.get("column", -1)
        if (row == -1):
            if (column == -1):
                row, column = index_random.Extend([], 2)
            else:
                column, row = index_random.Extend([column], 2)
        if (column == -1):
            if (row == -1):
                row, column = index_random.Extend([], 2)
            else:
                row, column = index_random.Extend([row], 2)

        assert row != column, 'Bad indecies'
        value = flags["value"] if "value" in flags else self.rand()
        return gen_FirstElementaryM(size, value, row, column)

    def InvertibleForm(self, size, flags):
        bounded = False
        if "bound" in flags:
            bounded = True
            bound = flags["bound"]
        sign_rand = Random(-1, 1).Filter(lambda x: x != 0)
        help_func = partial(self.__OneZeroUpperFunc__, self.rand, sign_rand)
        return gen_BoundedInvertibleM(size, bound, help_func) if bounded else gen_InvertibleM(size, help_func)

    # Help functions

    def __UniUpperFunc__(self, rand, row, column):
        if row == column:
            return 1
        elif row < column:
            return rand()
        else:
            return 0

    def __OneZeroUpperFunc__(self, rand, sign_rand, row, column):
        if row == column:
            return sign_rand()
        elif row < column:
            return rand()
        else:
            return 0
