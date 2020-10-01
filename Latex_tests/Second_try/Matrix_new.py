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

        if (self.form == 'SecondElementary'):
            assert "size" in flags, 'Size was not given'
            size = flags["size"]
            index_random = Random(0, size - 1)
            self.gen = partial(self.SecondElementaryForm,
                               index_random, size, flags)

        if (self.form == "ThirdElementary"):
            assert "size" in flags, 'Size was not given'
            size = flags["size"]
            index_random = Random(0, size - 1)
            self.gen = partial(self.ThirdElementaryForm,
                               index_random, size, flags)

        if (self.form == "Upper"):
            assert "size" in flags and "type" in flags, "Size or Type were not given"
            size = flags["size"]
            self.gen = partial(self.UpperForm, size, flags)

        if (self.form == "Invertible"):
            assert "size" in flags, 'Size was not given'
            size = flags["size"]
            self.gen = partial(self.InvertibleForm, size, flags)

        if (self.form == "Ranked"):
            assert "rows" in flags and "columns" in flags, 'Row and Columns were not given'
            rows = flags["rows"]
            columns = flags["columns"]
            rank = flags["rank"] if "rank" in flags else min(rows, columns)
            self.gen = partial(self.RankedForm, rows, columns, rank, self.rand)

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

    def SecondElementaryForm(self, index_random, size, flags):
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
        return gen_SecondElementaryM(size, row, column)

    def ThirdElementaryForm(self, index_random, size, flags):
        index = flags.get("index", index_random())
        assert 0 <= index < size, 'Bad index'
        value = flags["value"] if "value" in flags else self.rand()
        return gen_ThirdElementaryM(size, value, index)

    def UpperForm(self, size, flags):
        if flags["type"] == "IneZero":
            diag_rand = Random(0, 1)
            help_func = partial(self.__OneZeroUpperFunc__,
                                self.rand, diag_rand)
            return gen_OneZeroUpperM(size, help_func)
        else:
            help_func = partial(self.__UniUpperFunc__, self.rand)
            return gen_UniUpperM(size, help_func)

    def InvertibleForm(self, size, flags):
        bounded = False
        if "bound" in flags:
            bounded = True
            bound = flags["bound"]
        diag_rand = Random(-1, 1).Filter(lambda x: x != 0)
        help_func = partial(self.__OneZeroUpperFunc__, self.rand, diag_rand)
        return gen_BoundedInvertibleM(size, bound, help_func) if bounded else gen_InvertibleM(size, help_func)

    def RankedForm(self, rows, columns, rank, random):
        return gen_RankedM(rows, columns, rank, random)

    # Help functions

    def __UniUpperFunc__(self, rand, row, column):
        if row == column:
            return 1
        elif row < column:
            return rand()
        else:
            return 0

    def __OneZeroUpperFunc__(self, rand, diag_rand, row, column):
        if row == column:
            return diag_rand()
        elif row < column:
            return rand()
        else:
            return 0
