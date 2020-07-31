import Matrix_generators.py


class MatrixForm(object):
    def __init__(self, **flags):
        self.form = flags["form"]
        self.random = flags["random"]

        if (self.form == "FirstElementary"):
            self.data = gen_FirstElementary(size=flags["size"])
        if (self.form == "Secondlementary"):
            self.data = gen_SecondElementary(size=flags["size"])
        if (self.form == "ThirdElementary"):
            self.data = gen_ThirdElementary(size=flags["size"])
        if (self.form == "Permutation"):
            self.data = gen_PermutationM(size=flags["size"])
        if (self.form == "UniUpperWZ"):
            self.data = gen_UniUpperWZM(size=flags["size"])
        if (self.form == "UniUpperNZ"):
            self.data = gen_UniUpperNZM(size=flags["size"])
        if (self.form == "OneZeroUpperWZ"):
            self.data = gen_OneZeroUpperWZM(size=flags["size"])
        if (self.form == "OneZeroUpperNZ"):
            self.data = gen_OneZeroUpperNZM(size=flags["size"])
        if (self.form == "Invertible"):
            self.data = gen_InvertibleM(size=flags["size"])

    # helpers

    def __UniUpperWZFunc__(row, column):
        if row == column:
            return 1
        elif row < column:
            return self.random.BoundedWZ()
        else:
            return 0

    def __UniUpperNZFunc__(row, column):
        if row == column:
            return 1
        elif row < column:
            return self.random.BoundedNZ()
        else:
            return 0

    def __OneZeroUpperWZFunc__(row, column):
        if row == column:
            return self.random.Bool()
        elif row < column:
            return self.random.BoundedWZ()
        else:
            return 0

    def __OneZeroUpperNZFunc__(row, column):
        if row == column:
            return self.random.Bool()
        elif row < column:
            return self.random.BoundedNZ()
        else:
            return 0
